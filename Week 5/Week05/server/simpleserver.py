<<<<<<< HEAD
#!flask/bin/python
from flask import Flask

app = Flask ('__name__',
			static_url_path='',
			static_folder='../')

@app.route('/')
def index():
	return "Hello, World!"
	
if __name__ == '__main__':
=======
#!flask/bin/python
from flask import Flask

app = Flask ('__name__',
			static_url_path='',
			static_folder='../')

@app.route('/')
def index():
	return "Hello, World!"
	
if __name__ == '__main__':
>>>>>>> 955aac562b369b9e51df3a0f30a7478d09151948
	app.run(debug= True)