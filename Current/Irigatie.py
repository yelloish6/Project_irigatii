from Irigatie_param import *
from Irigatie_functions import *
import datetime
from time import sleep

currentDT = datetime.datetime.now()

start_time_h = [] #TODO remove these
start_time_m = [] #TODO remove these
rainSensorStatus = 1
#TEST MODE: in test mode, minutes are seconds for duration parameters
#TEST MODE: watering starts in the next minute, not when it is specified in Iriatie_param.py
#           watering duration is in seconds not in minutes

if function_mode == 'test':
	minute_multiplier = 1
	start_time_h.append(currentDT.hour)
	start_time_m.append(currentDT.minute+1)

elif function_mode == 'normal':
	minute_multiplier = 60
	for i in range(len(programs)):
		start_time_h.append(programs[i][0])
		start_time_m.append(programs[i][1])
else:
	print("ERROR: Unknown function mode")


#define local variables
humidity_log_interval_seconds = humidity_log_interval_minutes * minute_multiplier
humidity_log_interval = datetime.timedelta(seconds = humidity_log_interval_seconds)


#log all parameters

with open(log_path,'a') as f:
    f.write('Watering system starting on '+ str(currentDT)+'\n')
    f.write('Function mode '+ str(function_mode)+'\n')
    f.write('programs: '+ str(programs) +'\n')


#System Test: at system start-up, zone 2 is watered for 20 seconds
waterZoneOff(1)
waterZoneOff(2)
waterZoneOff(3)
waterZoneOff(4)
waterZone(2, 20)

#read humidity sensor and append value in the log
humidity_logtime = currentDT + humidity_log_interval

while True:
    currentDT = datetime.datetime.now()
    if currentDT > humidity_logtime:
        humidity_logtime = currentDT + humidity_log_interval
    if currentDT.minute == humidity_logtime.minute:
	rainSensorStatus = readRainSensor()
        with open(log_path,'a') as f:
            f.write(str(datetime.datetime.now()) + " " + str(rainSensorStatus) + "\n")
        humidity_logtime = humidity_logtime + humidity_log_interval
    #Start the sprinklers
    for i in range(len(programs)):
	#check what day of he week is it and if the program should run on this day
	if ((rainSensorStatus == 1) and
           (((int(currentDT.strftime("%w")) == 0) and (programs[i][8] == 1)) or
            ((int(currentDT.strftime("%w")) == 1) and (programs[i][2] == 1)) or
            ((int(currentDT.strftime("%w")) == 2) and (programs[i][3] == 1)) or
            ((int(currentDT.strftime("%w")) == 3) and (programs[i][4] == 1)) or
            ((int(currentDT.strftime("%w")) == 4) and (programs[i][5] == 1)) or
            ((int(currentDT.strftime("%w")) == 5) and (programs[i][6] == 1)) or
            ((int(currentDT.strftime("%w")) == 6) and (programs[i][7] == 1)))):
		if (currentDT.hour == start_time_h[i] and currentDT.minute == start_time_m[i]):
			for j in range(len(zones)):
				waterZone(j+1, programs[i][j+9]*minute_multiplier)
