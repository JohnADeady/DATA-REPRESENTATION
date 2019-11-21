#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response


app = Flask ('__name__', static_url_path='', static_folder='.')

# curl -i http://localhost:5000/deezer			
@app.route('/deezer', methods=['GET'])
def getAll():
    return jsonify( {deezer})
	
	
#curl -i http://localhost:5000/deezer/916424
@app.route('/deezer/<int:id>', methods =['GET'])
def getAll(id):
    foundId = list(filter(lambda t : t['id'] == id , deezer))
    if len(foundId) == 0:
        return jsonify( { 'deezer' : '' }),204
		
    return jsonify( { 'deezer' : foundId[0] })


	
if __name__ == '__main__' :
    app.run(debug= True)