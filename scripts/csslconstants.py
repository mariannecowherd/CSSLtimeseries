#!/usr/bin/env bash
## file to define values and folders


homedir = '/global/home/users/cowherd/cssltimeseries/'
rawdatadir = '/global/scratch/users/cowherd/CSSLdata/'
datadir = homedir + 'data/'

datakeys = ['Date', 'Air Temp Max (C)', 'Air Temp Min (C)',
       '24-hour Total Precip (mm)', 'Season Total Precip (mm)',
       '% of Precip as Snow', '% of Precip as Rain', 'New Snow (cm)',
       'Season Total Snow (cm)', 'Snowpack depth (cm)',
       'Snow Water Equivalent (cm)', 'Remarks', 'dt']