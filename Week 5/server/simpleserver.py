#!flask/bin/python
# Import flask
from flask import Flask

# App located in folder 
app = Flask ('__name__',
			static_url_path='',
			static_folder='../')

# create server that returns Hello World
@app.route('/')
def index():
	return "Hello, World!"

# if conditional statement is satisfied run function
if __name__ == '__main__':
	app.run(debug= True)