# Import mysql connector
import mysql.connector 

# My mysql credientals   
db = mysql.connector.connect(   
	host="127.0.0.1",   
	user="root",   
	password="Bruree06",
	auth_plugin='mysql_native_password',
	database="datarepresentation")
 
# Select all from table 
cursor = db.cursor()
sql="select * from student where id = %s" 
values = (1,) 

# Execute variables  
cursor.execute(sql, values) 

# Fetchall and print
result = cursor.fetchall() 
for x in result:   
	print(x) 
 