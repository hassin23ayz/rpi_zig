# this file will read digital values of the Zig 
# this file will read digital values of the Zig 
# this module is used by the main module 
from flask import current_app as app

class DigitalRead:
	@classmethod
	def get_button_state(self):
		return True

	def get_LDO_state(self):
		return False
