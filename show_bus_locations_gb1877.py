import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import sys

key=sys.argv[1]
line=sys.argv[2]
##This url connects MTA API server to the file
url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+key+"&VehicleMonitoringDetailLevel=calls&LineRef="+line
##Opening JSON file and converting it to a dataframe
lib=urllib.urlopen(url)
data=lib.read().decode('utf-8')
data=json.loads(data)
##number of active buses
count=len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
##Name of routes bus is currently active at
route=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['PublishedLineName']

print('Bus Line :',route,'\nNumber of active buses :',count)
##Manipulating data for its current coordinates
for i in range(count):
    loc=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']
    print('Bus ',i,' is at latitude ',loc['Latitude'],' and longitude ',loc['Longitude'])
