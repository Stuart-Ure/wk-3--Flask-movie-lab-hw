from flask import render_template, Blueprint, request
from models.movie_list import movies, add_new_movie
from models.movie import Movie


movies_blueprint = Blueprint("movies", __name__)

@movies_blueprint.route('/movies')
def index():
    return render_template('index.jinja', title= " Movie List", movies=movies)


@movies_blueprint.route('/movies', methods= ['POST'])
def add_movie():
    movie_title = request.form['title']
    movie_director = request.form['director']
    movie_genre = request.form['genre']
    new_movie=Movie(movie_title, movie_director, movie_genre) 

    add_new_movie(new_movie)
    return render_template('index.jinja', title= " Movie List", movies=movies)