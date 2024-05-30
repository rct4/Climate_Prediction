# Power Outage Prediction

### University of Illinois at Urbana-Champaign
### Climate Modeling, Prediction, and Applications

## Notebooks
[large_kdeplot](): Generates new kdeplots using larger dataset
(climet_lab)


## CDS API Requests
Using a processed datatable, the [request script](https://github.com/rct4/Climate_Prediction/blob/master/scripts/cds_request.py) is used to collect global ERA5 reanalysis data for each event date listed in the table. Data is saved in XArray format as NetCDF with [month]-[date]-[year].nc format. Due to large size, data stored locally on Keeling HPC.

## Data Visualization
Using this data, we are able to extract weather variables for each event. Saved data currently invludes 

Kernel density plots suggest common themes among power outage events. Results suggests ERA5 data may need certain sample sizes and regions to ensure accuracy when running ML models. 

![Kernel Density Plot Illinois](https://github.com/rct4/Climate_Prediction/blob/master/visuals/kdeplot/anom_pair_density_Illinois.png)

## Machine Learning Models
We are looking to classify power outage events by extreme weather type using K-means clustering. Results may suggest that certain severe weather events may be more likely to lead to power outage events.

We are also looking into the possibility of using Random Forest models to identify possible power outage events.