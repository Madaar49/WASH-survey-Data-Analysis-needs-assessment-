import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import Point, Polygon, shape, box
import matplotlib.pyplot as plt
import seaborn as sns
import math

class GeodataProcessor:
    def __init__(self, crs="EPSG:4326"):
        """
        Initialize GeodataProcessor with default CRS.
        """
        self.crs = crs

    def compute_area(self, gdf, field="area", crs=None):
        """Compute area in square kilometers of geometries in GeoDataFrame"""
        crs = crs if crs else self.crs
        gdf = gdf.to_crs(crs)
        gdf[field] = gdf.geometry.area / 10**6
        return gdf

    @staticmethod
    def convert_to_geodataframe(df, latitude, longitude):
        """
        Convert a DataFrame to GeoDataFrame with EPSG:4326 CRS.
        """
        geometry = [Point(xy) for xy in zip(df[longitude], df[latitude])]
        gdf = gpd.GeoDataFrame(df, geometry=geometry)
        gdf.set_crs(epsg=4326, inplace=True)
        return gdf
    
    def create_geodataframe(self, data, crs=None):
        """Create a GeoDataFrame"""
        crs = crs if crs else self.crs
        return gpd.GeoDataFrame(data, geometry=data["geometry"], crs=crs)

    @staticmethod
    def create_shapely_box(geom):
        """Create a bounding box using shapely"""
        minx, miny, maxx, maxy = geom.bounds
        return box(minx, miny, maxx, maxy)

    def create_tiles(self, gdf, width=1, length=1, file=None):
        """Create vector tiles from the total bounds of a GeoDataFrame"""
        xmin, ymin, xmax, ymax = self.geodataframe_bounds(gdf)
        cols = np.arange(xmin, xmax + width, width)
        rows = np.arange(ymin, ymax + length, length)

        polygons = [Polygon([(x, y), (x + width, y), (x + width, y + length), (x, y + length)])
                    for x in cols[:-1] for y in rows[:-1]]

        grid = self.create_geodataframe({'geometry': polygons})
        if file:
            grid.to_file(file)
        return grid

    @staticmethod
    def drop_columns_dataframe(gdf, columns):
        """Drop specified columns from GeoDataFrame or DataFrame"""
        available_columns = GeodataProcessor.get_columns_dataframe(gdf)
        remove_columns = [col for col in columns if col in available_columns]
        if remove_columns:
            return gdf.drop(remove_columns, axis=1)
        return gdf

    @staticmethod
    def get_columns(gdf):
        """Get all columns in GeoDataFrame or DataFrame"""
        return gdf.columns

    @staticmethod
    def geodataframe_bounds(gdf):
        """Return bounding box of GeoDataFrame"""
        return gdf.total_bounds

    def reproject_geodataframe(self, gdf, crs=None):
        """Reproject GeoDataFrame to another CRS"""
        crs = crs if crs else self.crs
        return gdf.to_crs(crs=crs)

    @staticmethod
    def spatial_join(gdf1, gdf2):
        """Perform a spatial join of two GeoDataFrames using intersect"""
        return gpd.sjoin(gdf1, gdf2, how="left", op="intersects")
    
    @staticmethod
    def spatial_join_pol_pts(gdf1, gdf2):
        """Spatial join a point and polygon GeoDataFrame using intersect"""
        joined_poly_pts = gpd.sjoin(gdf1, gdf2, how="inner", op="within")
        joined_poly_pts = joined_poly_pts.loc[:,
                                              ~joined_poly_pts.columns.str.endswith(
                                                  ('_left', '_right')
                                              )]
        return joined_poly_pts
    


def pivot_plot(gdf, aggregator, grid_cols=3):
        """
        Plot bar charts for each categorical column in the GeoDataFrame grouped by a specified category.
        """
        if aggregator not in gdf.columns:
            raise ValueError(f"Aggregator column '{aggregator}' not found in GeoDataFrame.")

        categorical_columns = gdf.select_dtypes(include=['object', 'category']).columns.tolist()
        if aggregator in categorical_columns:
            categorical_columns.remove(aggregator)

        if not categorical_columns:
            print("No categorical columns available for plotting.")
            return

        num_plots = len(categorical_columns)
        grid_rows = math.ceil(num_plots / grid_cols)

        fig_height = 5 * grid_rows
        fig_width = 5 * grid_cols
        fig, axes = plt.subplots(grid_rows, grid_cols, figsize=(fig_width, fig_height))
        
        if num_plots == 1:
            axes = [axes]
        else:
            axes = axes.flatten()

        for i, col in enumerate(categorical_columns):
            sns.countplot(data=gdf, x=col, hue=aggregator, ax=axes[i], palette="Set2")
            axes[i].set_title(f'Count of {col} by {aggregator}')
            axes[i].set_xlabel(col)
            axes[i].set_ylabel('Count')
            axes[i].tick_params(axis='x', rotation=45)
            if i % grid_cols == 0:
                axes[i].legend(title=aggregator, bbox_to_anchor=(1.05, 1), loc='upper left')
            else:
                axes[i].get_legend().remove()

        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])

        plt.tight_layout()
        plt.show()
        


def plot_categorical_columns(df, drop_columns=None, grid_cols=None, figsize=None):
    """
    Plot bar charts for each categorical column in the DataFrame.

    """
    # Drop specified columns if provided
    if drop_columns:
        df = df.drop(columns=drop_columns, axis=1, errors='ignore')

    # Identify categorical columns
    categorical_columns_names = df.select_dtypes(include=['object', 'category']).columns.tolist()

    if not categorical_columns_names:
        print("No categorical columns found in the DataFrame.")
        return
    
    num_plots = len(categorical_columns_names)
    grid_rows = math.ceil(num_plots / grid_cols)

    fig, axes = plt.subplots(grid_rows, grid_cols, figsize=(figsize[0],
                                                            figsize[1] * grid_rows))
    axes = axes.flatten()   

    for i, col in enumerate(categorical_columns_names):
        value_counts = df[col].value_counts()
        sns.barplot(x=value_counts.index, y=value_counts.values, ax=axes[i])
        axes[i].set_title(f'Distribution by {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Count')
        axes[i].tick_params(axis='x', rotation=90)

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()