import datetime
from gpiozero import LED, Button
from time import sleep
from Irigatie_param import *


def readRainSensor():
    print("Enter rain sensor value[0 or 1]:")
    sensor = Button(rain_sensor_pin)
    val = sensor.value
    print(sensor.value)
    return val

def waterZone(zone_selected,zone_watering_time):
	waterZone = LED(zones[zone_selected - 1])
	waterZone.off()
	with open(log_path,'a') as f: 
		f.write("Zone " + str(zone_selected) + " started at " + str(datetime.datetime.now()) + "\n") 
	sleep(zone_watering_time)
	waterZone.on()
	with open(log_path,'a') as f: 
		f.write("Zone " + str(zone_selected) + " stopped at " + str(datetime.datetime.now()) + "\n") 
	sleep(10)

def waterZoneOff(zone_selected):
	waterZone = LED(zones[zone_selected - 1])
	waterZone.on()
	

#turn all zones off - safety precaution
#    for i in range(len(zones)):
#	LED(zones[i]).on()
    #go through all the zones, and if it's the selected one, water for the required watering time and log the event.
#    for i in range(len(zones)):
#	if (zone_selected == i+1):
#		LED(zones[i]).off()
#		with open(log_path,'a') as f: 
#		   f.write("Zone " + str(zone_selected) + " started at " + str(datetime.datetime.now()) + "\n") 
#	       	sleep(zone_watering_time)
#		LED(zones[i]).on()
#		with open(log_path,'a') as f: 
#		   f.write("Zone " + str(zone_selected) + " stopped at " + str(datetime.datetime.now()) + "\n") 
#	        sleep(10)
