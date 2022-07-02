# this file is called main . 
# it is the frontend and the main controller of the app 
# this is used by the app module using flask blueprint pattern 
from flask import Blueprint, render_template
from flask import current_app as app
from .analog_read import AnalogRead
from .digital_read import DigitalRead

main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/")
def show():
	app.logger.info("Starting to retrieve data from analog_read & digital_read")

	aRead = AnalogRead()
	dRead = DigitalRead()

	button = dRead.get_button_state()
	ldo    = dRead.get_LDO_state()

	vcc    = aRead.get_vcc()
	vdd    = aRead.get_vdd()
	ldoV   = aRead.get_LDO()

	result = {
		"Button": button,
		"ldo"   : ldo,
		"vcc"   : vcc,
		"vdd"   : vdd,
		"ldoV"  : ldoV
	}

	app.logger.debug(f"Core data: {result}")

	return "hello from main ui"