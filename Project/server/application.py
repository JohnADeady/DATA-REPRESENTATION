#!flask/bin/python

# Import necessay libraries 
from flask import Flask, jsonify,  request, abort, make_response, render_template, redirect, url_for, request
from WTForms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from artistsDAO import artistsDAO 

# Search for server path
app = Flask ('__name__', static_url_path='', static_folder='.')
# Don't sort array
app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

nextId=3

# Use method GET to get all data
# curl -i http://localhost:5000/artists
@app.route('/artists')
def getAll():
    results = artistsDAO.getAll()
    return jsonify(results)
	
# Use method GET to get all data
# curl -i http://localhost:5000/albums
@app.route('/albums')
def getAllal():
    results = artistsDAO.getAllal()
    return jsonify(results)

# Use method GET to find data by id 
# curl -i http://localhost:5000/artists/1
@app.route('/artists/<int:id>', methods =['GET'])
def findByID(id):
    foundArtists = artistsDAO.findByID(id)

    return jsonify(foundArtists)
	
# Use method GET to find data by id 
# curl -i http://localhost:5000/artists/1
@app.route('/albums/<int:id>', methods =['GET'])
def findByIDal(id):
    foundAlbums = artistsDAO.findByIDal(id)

    return jsonify(foundAlbums)

# Use method POST to input new data 
# curl -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"Neil Young\",\"genre\":\"Folk Rock\",\"albums\":312}" http://localhost:5000/artists
@app.route('/artists', methods=['POST'])
def createartist():
    if not request.json:
        abort(400)
        
    artists = {
        "name": request.json['name'],
        "genre": request.json['genre'],
        "albums": request.json['albums']
    }
    features = (artists['name'],artists['genre'],artists['albums'])
    newId = artistsDAO.create(features)
    artists['id'] = newId
    
    return jsonify(artists),201
	
# Use method POST to input new data 
# curl -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"Neil Young\",\"genre\":\"Folk Rock\",\"albums\":312}" http://localhost:5000/artists
@app.route('/albums', methods=['POST'])
def createalbums():
    if not request.json:
        abort(400)
        
    albums = {
        "title": request.json['title'],
        "artist": request.json['artist'],
        "duration": request.json['duration']
    }
    feature = (albums['title'],albums['artist'],albums['duration'])
    newId = artistsDAO.createal(feature)
    albums['id'] = newId
    
    return jsonify(albums),201

# Use method PUT to dataset 
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"Fiesta\"}" http://localhost:5000/artists/123
@app.route('/artists/<int:id>', methods =['PUT'])
def updateartist(id):
    foundArtists = artistsDAO.findByID(id)
    if (len(foundArtists) == 0):
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    
    if 'albums' in request.json and type(reqJson['albums']) is not int:
        abort(400)
    
        
    if 'name' in reqJson:
        foundArtists['name'] = reqJson['name']
    if 'genre' in reqJson:
        foundArtists['genre'] = reqJson['genre']
    if 'albums' in reqJson:
        foundArtists['albums'] = reqJson['albums']
	
    features = (foundArtists['name'],foundArtists['genre'],foundArtists['albums'], foundArtists['id'])
    artistsDAO.update(features)
    return jsonify(foundArtists)
    
	
# Use method PUT to dataset 
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"Fiesta\"}" http://localhost:5000/artists/123
@app.route('/albums/<int:id>', methods =['PUT'])
def updatealbums(id):
    foundAlbums = artistsDAO.findByIDal(id)
    if (len(foundAlbums) == 0):
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    
    if 'duration' in request.json and type(reqJson['duration']) is not int:
        abort(400)
    
        
    if 'title' in reqJson:
        foundAlbums['title'] = reqJson['title']
    if 'artist' in reqJson:
        foundAlbums['artist'] = reqJson['artist']
    if 'duration' in reqJson:
        foundAlbums['duration'] = reqJson['duration']
	
    features = (foundAlbums['title'],foundAlbums['artist'],foundAlbums['duration'], foundAlbums['id'])
    artistsDAO.updateal(features)
    return jsonify(foundAlbums)
    	
# Use method DELETE to delete dataset
# curl -X DELETE "http://localhost:5000/artists/1000000"
@app.route('/artists/<int:id>', methods =['DELETE'])
def deleteartist(id):
    artistsDAO.delete(id)
        
    return  jsonify( { 'Completed':True })
	
# Use method DELETE to delete dataset
# curl -X DELETE "http://localhost:5000/artists/1000000"
@app.route('/albums/<int:id>', methods =['DELETE'])
def deletealbums(id):
    artistsDAO.deleteal(id)
        
    return  jsonify( { 'Completed':True })
	
@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return "Hello Boss!"

@app.route('/login', methods=['POST'])
def login():
	if request.form['password'] == 'password' and request.form['username'] == 'admin':
		session['logged_in'] = True
	else:
		flash('wrong password!')
	return home()
	
@app.route("/logout")
def logout():
	session['logged_in'] = False
	return home()

# error handling if data not found  
@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

# error handling if bad request
@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)

if __name__ == '__main__':
    app.run(debug= True)