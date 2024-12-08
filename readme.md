# BIXI Bike-Share Data Analysis
### COMP 3125 Individual Project, Wentworth Institute of Technology

## Description:

A project that analyzes Montreal bike share (Bixi) usage and predicts the usage of individual stations using data from prior years.

## Questions:

- Has there been an increase or decrease in ridership over the years, particularly in certain months/areas?
- Is Bixi ridership more heavily concentrated in parts of Montreal with an established bike lane network?
- Bixi recently introduced a cold-weather program this last year. Do people use the Bixi network in the winter? How sharp was the drop-off between summer and winter?
- Does the weather tend to change people's riding behavior? Do people take shorter trips during rainy/bad weather days, or just not ride at all?
- Is Bixi disproportionately used in "wealthier" or "touristy" arrondisements of Montreal, or is usage evenly distributed?
- Does proximity to a metro station affect ridership? Could we predict whether or not a metro station is nearby based on ride behavior?

## Datasets:

- Bixi has a fantastic dataset by year, containing every Bixi trip, start/end location, and duration.
https://bixi.com/en/open-data/
- The Canadian/Quebecois government has a good dataset with the location of all bike lanes in Montreal. It might be hard to get them by year built, but I'd be happy with just the most recent available data.
https://open.canada.ca/data/en/dataset/5ea29f40-1b5b-4f34-85b3-7c67088ff536
- The Canadian Census has median household income by electoral district, which roughly lines up with arrondisement.
https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/page.cfm?Lang=E&SearchText=Montreal&DGUIDlist=2021A00052466023&GENDERlist=1,2,3&STATISTIClist=1&HEADERlist=0
- The Canadian government has historical weather data by day.
https://climate.weather.gc.ca/historical_data/search_historic_data_e.html

## Setup:

Github has a file size upload restriction, and the Bixi datasets are extremely large. To get around this restriction, the datasets are available at the google drive link [here](https://drive.google.com/drive/folders/1iXZRpnqqPB-p0SiQs8PmBnktTJlV16Su?usp=sharing). Anyone with a Wentworth Institute Technology email address can access the link. Copy the files over from the downloaded folder into the data folder in the repository.
