# Import mysql connector
import mysql.connector 
 
# My mysql credientals
mydb = mysql.connector.connect(   
	host="localhost",   
	user="root",   
	password="Bruree06" ) 
 
mycursor = mydb.cursor() 

# Create a database 
mycursor.execute("CREATE DATABASE datarepresentation ") 