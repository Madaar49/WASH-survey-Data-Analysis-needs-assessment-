# Data processing and analysis of the WASH baseline survey in Sierra Leone 2016

## The WASH survey 2016 data
WASH is an acronym for (Water, sanitation and hygiene). The Sierra Leone WASH portal is a comprehensive mapping exercise carried out by the Ministry of Water Resources (MOWR) and its partners in 2016. Over 28,000 public improved waterpoints across all of Sierra Leone’s districts and chiefdoms have been mapped during this period. The exercise constitutes a comprehensive update of the earlier mapping in 2012.
The original data was retrieved from [washdata-sl.org](https://washdata-sl.org/wash-data/) in 2022. Since then the data on the website has been pre-processed and updated. I used the previous version (raw WASH baseline survey questionnaire) because it require more cleaning - better for gaining more experience.

## Contents
### Data and scripts
This repository includes the raw WASH baseline survey questionnaire,  pre-processing notebook and the post processed files. My initial idea was to develop a suitability predictive model to infer what type of water point is suitable in a geographical area. This work is still in progress, but I decided to showcase the processed data on a dashboard.
The data was processed using python, and the notebook can be accessed at [WASH_survey_preprocessing.ipynb](https://github.com/Madaar49/WASH-survey-Data-Analysis-needs-assessment-/blob/main/WASH_survey_preprocessing.ipynb).

### The dashboard
The dashboard was created using the post processed data, and hosted by the [The Africa GeoPortal](https://www.africageoportal.com). It can be accessed at [Sierra Leone water points Dashboard](https://africageoportal.maps.arcgis.com/apps/dashboards/912c78bb3e644e31a9976f847a4fd51a).
