from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# Must be here, otherwise circular import issue
from app import routes
