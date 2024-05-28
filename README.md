# Power Outage Prediction

### University of Illinois at Urbana-Champaign
### Climate Modeling, Prediction, and Applications

To Do:
Update summary, features, findings, examples, etc.

## CDS API Requests
Using a processed datatable, the [request script](https://github.com/rct4/Climate_Prediction/blob/master/scripts/cds_request.py) is used to collect global ERA5 reanalysis data for each event date listed in the table. Data is saved in XArray format with [month]-[date]-[year].nc format. Due to large size, data stored locally on Keeling HPC.

## Data Visualization
Kernel density plots suggest common themes among power outage events. Results suggests possible inconsistencies in ERA5 data. 