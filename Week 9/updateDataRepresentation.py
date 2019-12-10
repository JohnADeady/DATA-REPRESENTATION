# Import mysql connector
import mysql.connector 

# My mysql credientals  
db = mysql.connector.connect(   
	host="127.0.0.1",   
	user="root",   
	password="Bruree06",
	auth_plugin='mysql_native_password',
	database="datarepresentation")
 
 # Update into table 
cursor = db.cursor() 
sql="update student set name= %s, age=%s  where id = %s" 
values = ("Joe",33, 1) 

# Execute variables 
cursor.execute(sql, values) 

# Print when complete 
db.commit() 
print("update done") 