# this file will read analog values of the Zig 
from flask import current_app as app

class AnalogRead:
	@classmethod
	def get_vcc(self):
		vcc = 3.3
		app.logger.debug(f"vcc: {vcc}")
		return vcc

	@classmethod
	def get_vdd(self):
		return 3.2

	@classmethod
	def get_LDO(self):
		return 2.5
