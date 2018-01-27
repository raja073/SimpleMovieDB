
from flask import Flask, render_template 
app = Flask(__name__) ### Instance of the Flask with name of the running application as an argument

#################################################################################################
# Adding database to Flask application

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Movie, Actor

engine = create_engine('sqlite:///movieactors.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

#################################################################################################

@app.route('/')
@app.route('/movies')
def movieList():
	movies = session.query(Movie).all()
	return render_template('full_movie_list.html', movies = movies)


@app.route('/movie/<int:movie_id>/')
def movieActors(movie_id):
	movie = session.query(Movie).filter_by(id = movie_id).one()
	actors = session.query(Actor).filter_by(movie_id = movie.id)
	return render_template('menu.html', movie = movie, actors = actors)

# Task 1: Create route for newActor function here
@app.route('/movie/<int:movie_id>/new/')
def newActor(movie_id):
	return "Page to create new Actor. Task 1 complete"

# Task 2: Create route for editActor function here
@app.route('/movie/<int:movie_id>/<int:actor_id>/edit/')
def editActor(movie_id, actor_id):
	return "Page to edit new Actor. Task 2 complete"

# Task 3: Create route for deleteActor function here
@app.route('/movie/<int:movie_id>/<int:actor_id>/delete/')
def deleteActor(movie_id, actor_id):
	return "Page to delete new Actor. Task 3 complete"



if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)