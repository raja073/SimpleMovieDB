from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Movie, Actor

engine = create_engine('sqlite:///movieactors.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Movie Titanic
movie1 = Movie(name="Titanic")
session.add(movie1)
session.commit()

actor1 = Actor(name="Leonardo DiCaprio", gender="M", age="50", 
			biography="Few actors in the world have had a career quite as diverse as Leonardo DiCaprio's.", movie=movie1)
session.add(actor1)
session.commit()

actor2 = Actor(name="Kate Winslet", gender="F", age="45", 
			biography="Ask Kate Winslet what she likes about any of her characters, and the word is bound to pop up at least once.", movie=movie1)
session.add(actor2)
session.commit()

actor3 = Actor(name="Billy Zane", gender="M", age="55", 
			biography="William George Zane, better known as Billy Zane, was born on February 24, 1966 in Chicago, Illinois, to Thalia", movie=movie1)
session.add(actor3)
session.commit()

actor4 = Actor(name="Kathy Bates", gender="F", age="60", 
			biography="Multi-talented Kathleen Doyle Bates was born on June 28, 1948, and raised in Memphis, Tennessee.", movie=movie1)
session.add(actor4)
session.commit()

actor5 = Actor(name="Frances Fisher", gender="F", age="70", 
			biography="Frances Fisher began by apprenticing at the Barter Theatre in Abingdon, Virginia.", movie=movie1)
session.add(actor5)
session.commit()

# Movie Avatar
movie1 = Movie(name="Avatar")
session.add(movie1)
session.commit()

actor1 = Actor(name="Sam Worthington", gender="M", age="45", 
			biography="Samuel Henry John Worthington was born August 2, 1976 in Surrey, England.", movie=movie1)
session.add(actor1)
session.commit()

actor2 = Actor(name="Zoe Saldana", gender="F", age="35", 
			biography="Zoe Saldana was born on June 19, 1978 in Passaic, New Jersey, to Asalia Nazario and Aridio Salda.", movie=movie1)
session.add(actor2)
session.commit()

actor3 = Actor(name="Sigourney Weaver", gender="F", age="65", 
			biography="Sigourney Weaver was born Susan Alexandra Weaver in Leroy Hospital in Manhattan, New York City.", movie=movie1)
session.add(actor3)
session.commit()

actor4 = Actor(name="Stephen Lang", gender="M", age="60", 
			biography="A stage actor of great recognition, Stephen Lang has shaped a formidable career on and off the various stages", movie=movie1)
session.add(actor4)
session.commit()

actor5 = Actor(name="Michelle Rodriguez", gender="F", age="40", 
			biography="Known for tough-chick roles, Michelle Rodriguez is proof that there is a cross between beauty and brawn", movie=movie1)
session.add(actor5)
session.commit()

# Movie Gravity
movie1 = Movie(name="Gravity")
session.add(movie1)
session.commit()

actor1 = Actor(name="Sandra Bullock", gender="F", age="45", 
			biography="Sandra Annette Bullock was born in Arlington, a Virginia suburb of Washington, D.C.", movie=movie1)
session.add(actor1)
session.commit()

actor2 = Actor(name="George Clooney", gender="M", age="55", 
			biography="George Timothy Clooney was born on May 6, 1961, in Lexington, Kentucky, to Nina Bruce", movie=movie1)
session.add(actor2)
session.commit()

actor3 = Actor(name="Ed Harris", gender="M", age="75", 
			biography="By transforming into his characters and pulling the audience in, Ed Harris has earned a reputation as one ", movie=movie1)
session.add(actor3)
session.commit()

print "added movie items!"