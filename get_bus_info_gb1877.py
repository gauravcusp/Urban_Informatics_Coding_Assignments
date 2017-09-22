import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import sys
import csv
if not len(sys.argv)==4:
	print("Invalid number of arguments. Run as python <filename.py> <MTA Key> <BUS_LINE> <BUS_LINE>.csv")
	sys.exit()
key=sys.argv[1]
line=sys.argv[2]
file=sys.argv[3]

## Reading the data from MTA API where key and line are entered by the user
url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+key+"&VehicleMonitoringDetailLevel=calls&LineRef"+line

lib=urllib.urlopen(url)
data=lib.read().decode('utf-8')
data=json.loads(data)

count=len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

## Opening csv file, extracting required data and writing that data to a csv file
with open (file,'w') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow(['Latitude','Longitude','Stop Name','Stop Status'])
    for i in range(count):
        loc=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']
        if data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']=={}:
            stop='N/A'
        else:
            stop=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        if data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']=={}:
            status='N/A'
        else:
            status=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            
        writer=csv.writer(csv_file)
        
        ## Writing data to file
        writer.writerow([loc['Latitude'],loc['Longitude'],stop,status]) 

