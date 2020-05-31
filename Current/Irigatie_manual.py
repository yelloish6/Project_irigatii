#! /usr/bin/python
from gpiozero import LED
from time import sleep 
import datetime
import sys
import os
from Irigatie_param import *
from Irigatie_functions import *

#Call this script with following arguments: 
#	-zone to be watered [0-4] exceptions handled
#		[0] turn of all zones
#		[1-8] turn on specific zone
#	-duration to water that zone in SECONDS
zone_selected = int(sys.argv[1])
zone_watering_time = int(sys.argv[2])
#log_path = os.getcwd() + '/' + log_file

#New Code
if zone_selected == 0:
	for i in range(len(zones)):
		waterZoneOff(i)
elif 0 < zone_selected <= len(zones):
	waterZone(zone_selected,zone_watering_time)
else:
	print("ERROR: Selected watering zone does not exist")

#end NewCode


#zone1 = LED(zones[0])
#zone2 = LED(zones[1])
#zone3 = LED(zones[2])
#zone4 = LED(zones[3])
#zone1.on()
#zone2.on()
#zone3.on()
#zone4.on()


#if zone_selected == 1:
#	zone1.off()
#	with open(log_path,'a') as f: f.write("Zone " + str(zone_selected) + " started at " + str(datetime.datetime.now())  + "\n")
#	sleep(zone_watering_time)
#	LED(zones[0]).on()
#	with open(log_path,'a') as f: f.write("Zone " + str(zone_selected) + " stopped at " + str(datetime.datetime.now()) + "\n")
#	sleep(10)
#elif zone_selected == 2:
#	zone2.off()
#	with open(log_path,'a') as f: f.write("Zone " + str(zone_selected) + " started at " + str(datetime.datetime.now()) + "\n")
#	sleep(zone_watering_time)
#	zone2.on()
#	with open(log_path,'a') as f: f.write("Zone " + str(zone_selected) + " stopped at " + str(datetime.datetime.now()) + "\n")
#	sleep(10)
#elif zone_selected == 3:
#	zone3.off()
#	with open(log_path,'a') as f: f.write("Zone " + str(zone_selected) + " started at " + str(datetime.datetime.now()) + "\n")
#	sleep(zone_watering_time)
#	zone3.on()	
#	with open(log_path,'a') as f: f.write("Zone " + str(zone_selected) + " stopped at " + str(datetime.datetime.now()) + "\n")
#	sleep(10)
#elif zone_selected == 4:
#	zone4.off()
#	with open(log_path,'a') as f: f.write("Zone " + str(zone_selected) + " started at " + str(datetime.datetime.now()) + "\n")
#	sleep(zone_watering_time)
#	zone4.on()
#	with open(log_path,'a') as f: f.write("Zone " + str(zone_selected) + " stopped at " + str(datetime.datetime.now()) + "\n")
#	sleep(10)
#elif zone_selected == 0:
#	zone1.on()
#	zone2.on()
#	zone3.on()
#	zone4.on()
#else:
#	print("ERROR: Selected watering zone does not exist")
