#python pyvisa commands for controlling BK8600 series eloads

import pyvisa
import time
import easygui

# E-Load
class BK8600:
	# Initialize the BK8600 E-Load
	def __init__(self, resource_id = ""):
		rm = pyvisa.ResourceManager()
		
		if(resource_id == ""):
			resources = rm.list_resources()
			
			########### EASYGUI VERSION #############
			msg = "Select a visa resource for the E-Load:"
			title = "E-Load Selection"
			resource_id = choicebox(msg, title, resources)
			
			########### COMMAND LINE VERSION ########
			#print('{}\n'.format(resources))
			#id_index = input('Select resource list index\n')
			#resource_id = resources[id_index]
		
		self.inst = rm.open_resource(resource_id)
		print("Connected to %s\n" % self.inst.query("*IDN?"))
		#resets to Constant Current Mode
		self.inst.write("*RST")
		set_current(0)
		#set to remote mode (disable front panel)
		lock_front_panel(True)
		
	# To Set E-Load in Amps 
	def set_current(self, current_setpoint_A):		
		self.inst.write("CURR:LEV %s" % current_setpoint_A)

	def toggle_output(self, state):
		if state:
			self.inst.write("INP ON")
		else:
			self.inst.write("INP OFF")
	
	def remote_sense(self, state):
		if state:
			self.inst.write("REM:SENS ON")
		else:
			self.inst.write("REM:SENS OFF")
	
	def lock_front_panel(self, state):
		if state:
			self.inst.write("SYST:REM")
		else:
			self.inst.write("SYST:LOC")
	
	def measure_voltage(self):
		return float(self.inst.query("MEAS:VOLT:DC?"))

	def measure_current(self):
		return float(self.inst.query("MEAS:CURR:DC?"))
		
	def __del__(self):
		toggle_output(False)
		lock_front_panel(False)
		self.inst.close()
