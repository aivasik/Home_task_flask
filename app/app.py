from flask import Flask
from app.config import base_config
app = Flask(__name__)

app.config.update(**base_config)

from app.views import index, register

app.add_url_rule('/', view_func=index)
app.add_url_rule('/index', view_func=index)
app.add_url_rule('/register', view_func=register, methods=("GET", "POST"))
