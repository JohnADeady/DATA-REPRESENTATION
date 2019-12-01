#!flask/bin/python

# Import necessay libraries 
from flask import Flask, jsonify,  request, abort, make_response
from artistsDAO import artistsDAO 

# Search for server path
app = Flask ('__name__', static_url_path='', static_folder='.')
# Don't sort array
app.config['JSON_SORT_KEYS'] = False


artists = [
    {
        "id":1,
        "name":"Eminem",
        "genre":"Hip Hop",
        "albums":124
    },
    
    {
        "id":2,
        "name":"Neil Young",
        "genre":"Folk Rock",
        "albums":18
    }
]
nextId=3

# Use method GET to get all data
# curl -i http://localhost:5000/artists
@app.route('/artists')
def getAll():
    results = artistsDAO.getAll()
    return jsonify(results)

# Use method GET to find data by id 
# curl -i http://localhost:5000/artists/1
@app.route('/artists/<int:id>', methods =['GET'])
def findByID(id):
    foundArtists = artistsDAO.findByID(id)

    return jsonify(foundArtists)

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
    
# Use method DELETE to delete dataset
# curl -X DELETE "http://localhost:5000/artists/1000000"
@app.route('/artists/<int:id>', methods =['DELETE'])
def deleteartist(id):
    artistsDAO.delete(id)
        
    return  jsonify( { 'Completed':True })

# error handling if data not found  
@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

# error handling if bad request
@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)

if __name__ == '__main__' :
    app.run(debug= True)