Welcome the the Irigatii project:

**************
*** Files  ***
**************

Irigatie.py 
	--> main application file for the project

Irigatie_param.py <-- #TODO: add manual mode, and all parameters in the system
	--> parameters file containing all set-up parameters

Irigatie_functions.py <-- #TODO: move mappings to Irigatie_param.py
	--> collection of called functions:
		-readRainSensor() //reads the rain sensor value
		-waterZone(zone_selected,zone_watering_time) //contains also the mapping of the watering zones to pins

Irigatie_manual.py 
	--> run this file in command line to manually activate the watering zones. 
		#Call this script with following arguments: 
		#	-zone to be watered [0-4] exceptions handled
		#		[0] turn of all zones
		#		[1-4] turn on specific zone
		#	-duration to water that zone in SECONDS

**************
*** Deploy ***
**************

Create a floder on the target with the name of the previous version and copy everyrhing there
Copy from PC to target all the files directly in the Project_irigatii folder
!!!! do not copy the gpiozero.py file!!! 
Configure the Irigatii_param.py file to match your watering program

