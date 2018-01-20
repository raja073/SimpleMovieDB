import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

######################################################

class Movie(Base):

	__tablename__ = 'movie'

	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)

class Actor(Base):

	__tablename__ = 'actor'

	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	gender = Column(String(80))
	age = Column(Integer)
	biography = Column(String(250))
	movie_id = Column(Integer, ForeignKey('movie.id'))
	movie = relationship(Movie)

######################################################

engine = create_engine('sqlite:///movieactors.db')

Base.metadata.create_all(engine)






