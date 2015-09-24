import datetime
import json
import sys
import urllib2

if __name__=="__main__":
	url='http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % ((sys.argv[1]),(sys.argv[2]))
	request=urllib2.urlopen(url)
	metadata=json.loads(request.read())
	#jsonFile=open(sys.argv[1],'r')
	#mta=json.load(jsonFile)
	a=metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
	print (sys.argv[2])
	print 'The number of active bus lines are',len(a)
	for i in range(len(a)):
		lat= metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
		lon= metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
		print "Bus",i," is at latitude ",lat,"and longitude ",lon




	#for item in a:
		#print item
		#print ""

	#print a
	#print len(a)

