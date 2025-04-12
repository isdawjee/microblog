from flask import Flask

app = Flask(__name__)

# Must be here, otherwise circular import issue
from app import routes
