# Sierra Leone WASH survey 2016 ArcGIS dashboard

## Motivation
I wanted to work with data from my country, Sierra Leone, while putting my skill into practice. My initial idea was to develop a suitability predictive model to infer what type of water point is suitable in a geographical area. Although this work is still in progress, I decided to showcase  the processed data on a dashboard.

### Data used
This dashboard was created using the [processed Sierra Leone WASH 2016 survey data](https://github.com/Madaar49/WASH-survey-Data-Analysis-needs-assessment-/blob/main/WP_ALL%20DATA/WP%20Master.csv). WASH is an  acronym for (Water, sanitation and hygiene). The original data was retrieved from [washdata-sl.org](https://washdata-sl.org/wash-data/) in 2022. Since then the data on the website has been pre-processed and updated. I used the previous version because it require more cleaning - better for gaining more experience. 

### Data processing
The data was processed using python, and the notebook can be accessed at [WASH_survey_preprocessing.ipynb](https://github.com/Madaar49/WASH-survey-Data-Analysis-needs-assessment-/blob/main/03-Data%20Analysis.ipynb)

### Attributes selected
The original dataset contains 52 fields/attributes, and not all were choosen. The attribute information are specified below. The format is ('original column name' : `processed column name`)

* `chiefdom`
* `District`
* `Region`
* ('Submission Date':`sub_date`)
* ('2420047|Latitude': `latitude`)
* ('--GEOLON--|Longitude: `longitude`)
* ('7430032|Water point Name':`wp name`)
* ('4420041|Extraction system type': `extract_type`)
* ('5450040|Type of water point':`wp_type`)
* ('7430035|Water point Functionality': `wp_func`)
* ('4390041|Is water available throughout the year?': `wp_sustain`)
* ('6430039|Is/was this point monthly or regularly chlorinated?' :`chlorination`) 
* ('4430055|Year of construction': `const_year`)
* ('4390044|Who owns the water point?': `ownership`)
* ('7430040|Is there a trained mechanic available at this point?': `wp_mechanic`)
* ('4380054|Who is maintaining the water point (routine repairs)?': `maintenance`)
* ('7380052|Is there a WASH management committee?': `WASH_team`)
* ('460037|How many minutes does it take to reach the nearest spare part supplier?': `t_toSpares?`)
* (1500002|Has the community been declared ODF?': `commu_ODF?`)


## The Dashboard
Below you can find the details of the dashboard.It also serves as a guide on how to navigate and use the water point ArcGIS Dashboard effectively. 

### Accessing the Dashboard
The dashboard can be accessed at the [website](https://gbondo-am.github.io). 

### Choice of design and data displayed
I wanted to create a design as minimal as possible, but shows important information. I decided to display 5 fields which can be updated based on query. 

- Filters: To show waterpoint data based on a selected filter/query. It can be regional, district, or chiefdom admistrative level.

- Fields: I used 5 fields to display, all of which are focused on waterpoint characteristics. The idea was to have these values update based on filter.

    - Water points: to show the amount of water points.
    - WASH teams functional: to know the amount of WASH teams active. n/b A WASH team, commonly referred to as a `WASH Committee` consists of members elected by the community who are responsible for keeping the water supply, sanitation and hygiene facilities and services operational.
    - wp functionality: stands for water point functionality. To know the status of the water point, if in full operational or otherwise. Displays as a barchart.
   - water point type: shows the distribution of water point type, displayed as a barchart.
   - Year round sustainability: to know if there is adequate water in the water point throughout the year. Seasonal, in terms of water well means during the dry seasons, the water level drops down so low that it is insufficient to serve its community.

### Understanding the interface

![alt text](/images/main.PNG)
<p align="center">
<em>Water point 2016 dashboard</em>
</p>

#### Header Bar
**Title:** Displays the name of the dashboard.

#### Map View
Water point, District and Chiefdom data at the center of the dashboard. Zoom in/out buttons is located in bottom right, or you can scroll to zoom.

**Control buttons:** At the top right of the map view. Contains Home, legend, map layers and basemaps (such as satellite view, OSM, terrain etc.). 

#### Sidebar Panels:
 - **Filters Panel:** Allows you to filter data by various criteria (e.g., Region, district and chiefdom). The view pans into the selected filter area and shows all the water points within the area boundary. Additioinally, the Data summary panel is also updated based on filter

 - **Data Summary Panel:** Provides a summary of key statistics (e.g., water points, and WASHteam functionality). At the bottom you can choose which distribution you want to see. The options are (wp Functionality, water point type and year round sustainability) Values are updated based on filters choosen.

    - Download option: The filtered summary data for the charts can be downloaded in the form of a CSV file.

#### Pop-Up Information:
Clicking on a water point on the map opens a pop-up showing attribute information. 

![alt text](/images/point.png)
<p align="center">
<em>Popup information</em>
</p>