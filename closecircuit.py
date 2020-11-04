class Ohms_law_cal:
	
	def __init__(self, V, I, R, call_id):
		self.V = V
		self.I = I
		self.R = R
		self.call_id = call_id
		
	def caller(self):
		if self.call_id == "volts":
			return self.volts(self.I, self.R)
		elif self.call_id == "amps":
			return self.amps(self.V, self.R)
		elif self.call_id == "ohm":
			return self.ohm(self.V, self.I)
		else:
			print("unknown input")
		
	def volts(self, I, R):
		return I * R
		
	def amps(self, V, R):
		return V/R
		
	def ohm(self, V, I):
		return V/I
				
x = Ohms_law_cal(9, 0.2, 0, "ohm")
print(x.caller())