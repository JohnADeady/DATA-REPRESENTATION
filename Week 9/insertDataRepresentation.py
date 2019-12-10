# Import mysql connector
import mysql.connector 

# My mysql credientals 
db = mysql.connector.connect(   
	host="127.0.0.1",   
	user="root",   
	password="Bruree06",
	auth_plugin='mysql_native_password',
	database="datarepresentation")
 
 # Insert into table
cursor = db.cursor() 
sql="insert into student (name, age) values (%s,%s)" 
values = ("Mary",21) 

# Execute in mysql 
cursor.execute(sql, values) 
 
# Complete when done on last line 
db.commit()
print("1 record inserted, ID:", cursor.lastrowid) 