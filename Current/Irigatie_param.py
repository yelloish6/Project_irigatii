# Irigatie_param.py
import os

#****Function Mode****
#	'normal'- as it should be
#	'test'	- waterming duration is in seconds, not in minutes, use this to test the system with the sprinklers
#		do not turn the zones on for less than 5 seconds

function_mode = 'test'


#****mappings_on_hardware****
#17 zona de picurator
#18 gazon mare spre alee
#3 gazon mare in spate
#4 gazon mic

zones = [18,3,4,17] #zone 1,2,3,4...
rain_sensor_pin=21

#****Define programs******
# first 2 numbers: start time hour, start time minute
# days of the week when the program should start: 1 for active, 0 for inactive
# next numbers: zone durations in minutes, mappped with "zones" variables 
# !!WARNING!! the number of defined minutes must be the same as the number of zones
#            start hour| start minute|Mon|Tue|Wed|Thu|Fri|Sat|Sun|Zones duration  
programs = [[6 ,         0 ,           1,  0,  1,  0,  1,  0,  0,  20, 20, 20, 0 ],
	    [7 ,         30,           1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  20],	
            [21,         00,           1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  20]]

#****Name of file where to save logs*****
log_file = "Irigatii_log.txt"
log_path = os.getcwd() + '/' + log_file

#****Frequency to poll humidity sensor*****
humidity_log_interval_minutes = 15
