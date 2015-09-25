import datetime
import json
import sys
import urllib2
import csv

if __name__=="__main__":
	url='http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % ((sys.argv[1]),(sys.argv[2]))
	request=urllib2.urlopen(url)
	metadata=json.loads(request.read())
	print sys.argv[3]
	a=metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
	#jsonFile=open(metadata.json,'r')
	#metadata=json.load(metadata.json)
	#data=mta["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

	with open(sys.argv[3], 'wb') as B52:
		writer=csv.writer(B52)
		headers=['Latitude','Longitude','Stop Name','Stop Status']
		writer.writerow(headers)


		for i in range(len(a)):

			lat= metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
			lon= metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
			stopName=metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["MonitoredCall"]["StopPointName"]
			BusStatus=metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]

			writer.writerow([lat,lon,stopName,BusStatus])
		#print B52.readlines()
	afile= open('B52.csv','r+')
	csvReader1 = csv.reader(afile)
  	for i in range(len(a)):

  		print csvReader1.next()	
			

		
	
