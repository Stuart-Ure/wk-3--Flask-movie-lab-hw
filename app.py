from flask import Flask
from controller.movie_controller import movies_blueprint

app = Flask(__name__)
app.register_blueprint(movies_blueprint)