# Import mysql connector
import mysql.connector 
 
# My mysql credientals
db = mysql.connector.connect(   
	host="127.0.0.1",   
	user="root",   
	password="Bruree06",
	auth_plugin='mysql_native_password',
	database="datarepresentation")
 
# Delete based on id
cursor = db.cursor() 
sql="delete from student where id = %s" 
values = (1,) 

# execute to mysql 
cursor.execute(sql, values) 
 
 # Print when complete
db.commit() 
print("delete done") 
  