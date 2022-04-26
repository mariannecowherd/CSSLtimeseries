#!/usr/bin/env bash
## file to define values and folders
import os
import geopandas as gpd
import rasterio as rio
import pandas as pd
import glob
import pickle
import numpy as np
from csslconstants import * 

os.chdir(homedir)

rawdatadir = '/global/scratch/users/cowherd/CSSLdata/'

files = glob.glob(rawdatadir + '*.csv')
datakeys = ['Date', 'Air Temp Max (C)', 'Air Temp Min (C)',
       '24-hour Total Precip (mm)', 'Season Total Precip (mm)',
       '% of Precip as Snow', '% of Precip as Rain', 'New Snow (cm)',
       'Season Total Snow (cm)', 'Snowpack depth (cm)',
       'Snow Water Equivalent (cm)', 'Remarks', 'dt']

df = {}
for fn in files:
    data=pd.read_csv(fn)
    data = data.replace('--',np.nan)
    data = data.replace('T',np.nan)
    data.keys = datakeys
    data['dt'] = pd.to_datetime(data['Date'])
    data['Snow Water Equivalent (cm)'] = data['Snow Water Equivalent (cm)'].astype('float')
    year = ''.join(filter(lambda i: i.isdigit(), fn))
    df[year] = data

with open(datadir + 'cssldata.pickle', 'wb') as handle:
    pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)

print('saved CSSL data for ' + str(len(df)) + 'years')