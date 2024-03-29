import cdsapi
import climetlab as cml
import numpy as np
import matplotlib.pyplot as plt
import geopandas
import geopy
import xarray as xr
import sys

import csv
import os
import pickle

final_table = []

with open('../../a/era5_data/final_table.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    for line in csvFile:
        final_table.append(line)


stored_table = []
c = cdsapi.Client()
for row in final_table:
    print("run")
    if (row['Month'] + '-' + row['Day'] + '-' + row['Year']) in stored_table:
        continue
    print(row["Location"])
    print(row["Day"])
    print(row["Month"])
    print(row["Year"])
    print(row["ID"])
    c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis', 'format': 'netcdf', #netcdf
        'year': [
        row["Year"],
        ],
        'month': [
        row["Month"]
        ],
        'day': [
        row["Day"]
        ],
        'time': [
        '00:00', '03:00', '06:00', '09:00',
        '12:00', '15:00', '18:00', '21:00'
        ],
        'variable': [
        '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_temperature',
        'snowfall', 'surface_pressure', 'total_precipitation',
        ],
        },
        '../../a/era5_data/' + row['Month'] + '-' + row['Day'] + '-' + row['Year'] + '.nc')
    stored_table.append(row['Month'] + '-' + row['Day'] + '-' + row['Year'])
