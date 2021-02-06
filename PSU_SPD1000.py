#python pyvisa commands for controlling Siglent SPD1000 series power supplies

import pyvisa
import time
import easygui

# Power Supply
class SPD1000:
	# Initialize the SPD1000 Power Supply
	def __init__(self, resource_id = ""):
		rm = pyvisa.ResourceManager()
		
		if(resource_id == ""):
			resources = rm.list_resources()
			
			########### EASYGUI VERSION #############
			msg = "Select a visa resource for the Power Supply:"
			title = "Power Supply Selection"
			resource_id = choicebox(msg, title, resources)
			
			########### COMMAND LINE VERSION ########
			#print('{}\n'.format(resources))
			#id_index = input('Select resource list index\n')
			#resource_id = resources[id_index]
		
		self.inst = rm.open_resource(resource_id)
		print("Connected to %s\n" % self.inst.query("*IDN?"))
		self.inst.write("*RST") #resets to Constant Current Mode
		#Choose channel 1
		self.inst.write("INST CH1")
		#lock front panel
		lock_front_panel(True)
		set_current(0)
		set_voltage(0)
		
	# To Set E-Load in Amps 
	def set_current(self, current_setpoint_A):		
		self.inst.write("CURR {}".format(current_setpoint_A))

	def set_voltage(self, voltage_setpoint_V):
		self.inst.write("VOLT {}".format(voltage_setpoint_V))

	def toggle_output(self, state):
		if state:
			self.inst.write("OUTP ON")
		else:
			self.inst.write("OUTP OFF")
	
	def remote_sense(self, state):
		if state:
			self.inst.write("MODE:SET 4W")
		else:
			self.inst.write("MODE:SET 2W")
	
	def lock_front_panel(self, state)
		if state:
			self.inst.write("*LOCK")
		else:
			self.inst.write("*UNLOCK")
	
	def measure_voltage(self):
		return float(self.inst.query("MEAS:VOLT?"))

	def measure_current(self):
		return float(self.inst.query("MEAS:CURR?"))
		
	def measure_power(self):
		return float(self.inst.query("MEAS:POWE?"))
		
	def __del__(self):
		toggle_output(False)
		lock_front_panel(False)
		self.inst.close()
