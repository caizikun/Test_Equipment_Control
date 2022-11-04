#python implementation for a fake power supply to test programs - has all functions and returns some values

# E-Load
class Fake_Eload:
	
	has_remote_sense = False
	self.mode = "CURR"

	def __init__(self, resource_id = None):
		self.max_power = 10000
		self.max_current = 1000
		
		pass
		
	# To Set E-Load in Amps 
	def set_current(self, current_setpoint_A):
		if self.mode != "CURR":
			print("ERROR - E-load not in correct mode")
		pass
	
	def set_mode_current(self):
		self.mode = "CURR"
	
	def set_mode_voltage(self):
		self.mode = "VOLT"
		pass
		
	def set_cv_voltage(self, voltage_setpoint_V):
		if self.mode != "VOLT":
			print("ERROR - E-load not in correct mode")
		pass
	
	def toggle_output(self, state):
		pass
	
	def remote_sense(self, state):
		pass
	
	def lock_front_panel(self, state):
		pass
	
	def measure_voltage(self):
		return 4.05

	def measure_current(self):
		return -1.0
