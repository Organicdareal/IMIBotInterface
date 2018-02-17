from flask import Flask
app = Flask(__name__)
import IMIBotInterface.views
from IMIBotInterface.ControlsHandler import ControlsHandler


with app.app_context():
    handler = ControlsHandler()
