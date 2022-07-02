# app module has the flask app pattern
# app module energies main module by flasK blueprint pattern
#     so that the main module can have route functionality 
import logging

from flask import Flask
from logging.handlers import RotatingFileHandler
from .main import main_blueprint

def create_app(config_file="config/local_config.py"):
    app = Flask(__name__)  # Initialize app
    app.config.from_pyfile(config_file, silent=False)  # Read in config from file

    # Configure file based log handler
    log_file_handler = RotatingFileHandler(
        filename=app.config.get("LOG_FILE_NAME", "config/pi-car.log"),
        maxBytes=10000000,
        backupCount=4,
    )
    log_file_handler.setFormatter(
        logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
    )
    app.logger.addHandler(log_file_handler)
    app.logger.setLevel(app.config.get("LOGGER_LEVEL", "ERROR"))
    app.logger.info("----- STARTING APP ------")
    app.register_blueprint(main_blueprint)

    # @app.route("/")
    # def hello_world():
    #     app.logger.info("Running first route")
    #     # return "Hello, World!"
    #     sens = AnalogRead()
    #     vcc = sens.get_vcc()

    #     dg = DigitalRead()
    #     dr = dg.get_button_state()

    #     ret = str(vcc) + " " + str(dr)
    #     return str(ret)

    app.logger.info("----- FINISHED STARTING APP -----")

    return app
