import random
import datetime

class LED:
	def __init__(self, pin):
		self.pin = pin
		self.value = 0
	
	def on(self):
		self.value = 1
		print(str(datetime.datetime.now()) + ": Setting pin " + str(self.pin) + " on. " + str(self.value))
		
	def off(self):
		self.value = 0
		print(str(datetime.datetime.now()) + ": Setting pin " + str(self.pin) + " off. " + str(self.value))

class Button:
	def __init__(self, pin):
		self.pin = pin
		self.value = 0

	def value(self):
		self.value = random.randrange(0,1)
#		self.value = input()
#		print(str(datetime.datetime.now()) + ": The value of the button " + str(self.pin) + " is " + str(self.value))

