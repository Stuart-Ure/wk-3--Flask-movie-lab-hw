from models.movie import Movie

movie1 = Movie( 'Jaws', 'Steven Spielberg', 'thriller')
movie2 = Movie('Openheimer','Christopher Nolan', 'war')
movie3= Movie('Barbie', 'Greta Gerwig', 'comedy') 
movie4=Movie ('Deadpool', 'Tim Miller', 'Action')

movies=[movie1, movie2, movie3, movie4]

def add_new_movie(movie):
    movies.append(movie)