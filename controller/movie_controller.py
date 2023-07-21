from flask import render_template, Blueprint, request
from models.movie_list import movies, add_new_movie
from models.movie import Movie


movies_blueprint = Blueprint("movies", __name__)

@movies_blueprint.route('/movies')
def index():
    return render_template('index.jinja', title= " Movie List", movies=movies)