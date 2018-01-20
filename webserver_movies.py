from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

############ DB Connection #############################################################
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Movie, Actor

engine = create_engine('sqlite:///movieactors.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
########################################################################################
class webserverHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		try:
			if self.path.endswith("/movie/new"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>"
				output += "<h1>Make a New Movie</h1>"
				output += '''<form method='POST' enctype='multipart/form-data' action='movie/new'>'''
				output += '''<input name='newMovieName' type='text' placeholder = 'New Movie Name'>'''
				output += '''<input type='submit' value='Create'>'''
				output += "</body></html>"
				self.wfile.write(output)
				return

			if self.path.endswith("/edit"):
				movieIDPath = self.path.split("/")[2]
				myMovieQuery = session.query(Movie).filter_by(id = movieIDPath).one()
				if myMovieQuery != []:
					self.send_response(200)
					self.send_header('Content-type', 'text/html')
					self.end_headers()

					output = ""
					output += "<html><body>"
					output += "<h1>myMovieQuery.name</h1>"
					output += '''<form method='POST' enctype='multipart/form-data' action='/movies/%s/edit'>''' % movieIDPath
					output += '''<input name='newMovieName' type='text' placeholder='%s'>''' % myMovieQuery.name
					output += '''<input type='submit' value='Rename'>'''
					output += "</form>" 
					output += "</body></html>"
					self.wfile.write(output)


			if self.path.endswith("/delete"):
				movieIDPath = self.path.split("/")[2]
				myMovieQuery = session.query(Movie).filter_by(id = movieIDPath).one()
				if myMovieQuery != []:
					self.send_response(200)
					self.send_header('Content-type', 'text/html')
					self.end_headers()

					output = ""
					output += "<html><body>"
					output += "<h1>Are you sure you want to Delete: %s</h1>" % myMovieQuery.name
					output += '''<form method='POST' enctype='multipart/form-data' action='/movies/%s/delete'>''' % movieIDPath
					output += '''<input type='submit' value='Delete'>'''
					output += "</form>" 
					output += "</body></html>"
					self.wfile.write(output)
	

			if self.path.endswith("/movies"):
				movies = session.query(Movie).all()
				#output = ""
				#output += "<a href = 'movie/new'> Make a new Movie Here </a></br></br>"
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>"
				output += "<a href = 'movie/new'> Make a new Movie Here </a></br></br>"
				for movie in movies:
					output += movie.name
					output += "</br>"
					output += "<a href = '/movie/%s/edit'>Edit</a>" % movie.id
					output += "</br>"
					output += "<a href = '/movie/%s/delete'>Delete</a>" % movie.id
					output += "</br></br>"
				output += "</body></html>"
				self.wfile.write(output)
				return

			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>Hello!!"
				output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
				output += "</body></html>"
				self.wfile.write(output)
				print output
				return

			if self.path.endswith("/hola"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>Hola!!"
				output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
				output += "</body></html>"
				self.wfile.write(output)
				print output
				return

		except IOError:
			self.senf_error(404, "File not found %s" % self.path)

	def do_POST(self):
		try:
			if self.path.endswith("/movie/new"):
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
			 	messagecontent = fields.get('newMovieName')

			 	# Create new movie class
			 	newMovie = Movie(name = messagecontent[0])
			 	session.add(newMovie)
			 	session.commit()

			 	self.send_response(301)
			 	self.send_header('Content-type', 'text/html')
			 	self.send_header('Location', '/movies')
			 	self.end_headers()

			if self.path.endswith("/edit"):
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
			 	messagecontent = fields.get('newMovieName')
			 	movieIDPath = self.path.split("/")[2]

			 	myMovieQuery = session.query(Movie).filter_by(id=movieIDPath).one()
			 	if myMovieQuery != []:
			 		myMovieQuery.name = messagecontent[0]
			 		session.add(myMovieQuery)
			 		session.commit()

			 		self.send_response(301)
			 		self.send_header('Content-type', 'text/html')
			 		self.send_header('Location', '/movies')
			 		self.end_headers()

			if self.path.endswith("/delete"):
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			 	movieIDPath = self.path.split("/")[2]
			 	myMovieQuery = session.query(Movie).filter_by(id=movieIDPath).one()

			 	if myMovieQuery != []:
			 		session.delete(myMovieQuery)
			 		session.commit()
			 		self.send_response(301)
			 		self.send_header('Content-type', 'text/html')
			 		self.send_header('Location', '/movies')
			 		self.end_headers()

		except:
			pass




def main():
	try:
		port = 8080
		server = HTTPServer(('', port), webserverHandler)
		print "Web server is running on port: %s" % port
		server.serve_forever()


	except KeyboardInterrupt:
		print "^C entered, stopping webserver...!!"
		server.socket.close()



if __name__ == '__main__':
	main()