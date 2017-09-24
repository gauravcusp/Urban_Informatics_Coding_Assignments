import pandas as pd
import numpy as np
import pylab as pl
%pylab inline

fout=pd.read_csv('/gws/open/NYCOpenData/nycopendata/data/h9gi-nx95/1482192000/h9gi-nx95.csv')
df1=pd.DataFrame
print("Raw Data: \n",fout.head)

#Dropping other columns
fout.drop(['DATE', 'TIME', 'BOROUGH', 'ZIP CODE', 'LOCATION', 'ON STREET NAME', 'CROSS STREET NAME', 'OFF STREET NAME','NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED','NUMBER OF PEDESTRIANS INJURED', 'NUMBER OF PEDESTRIANS KILLED','NUMBER OF CYCLIST INJURED', 'NUMBER OF CYCLIST KILLED','NUMBER OF MOTORIST INJURED', 'NUMBER OF MOTORIST KILLED','CONTRIBUTING FACTOR VEHICLE 1', 'CONTRIBUTING FACTOR VEHICLE 2','CONTRIBUTING FACTOR VEHICLE 3', 'CONTRIBUTING FACTOR VEHICLE 4','CONTRIBUTING FACTOR VEHICLE 5', 'UNIQUE KEY', 'VEHICLE TYPE CODE 1','VEHICLE TYPE CODE 2', 'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4','VEHICLE TYPE CODE 5'],axis=1,inplace=True)

for i in range(len(fout)):
    if fout['LATITUDE'][i]==0:
        fout['LATITUDE'][i]=np.nan
    if fout['LONGITUDE'][i]==0:
        fout['LONGITUDE'][i]=np.nan
        
#Dropping all the NaN values
df=fout.dropna(how='all')   

  
print("Data with just two rows: \n",df.head)


#Plotting the graph between latitude and longitude
pl.plot(df['LATITUDE'][:],df['LONGITUDE'][:],'.')
pl.xlabel('Latitude')
pl.ylabel('Longitude')
pl.title('Plot between the longitude and latitude of each collision')
