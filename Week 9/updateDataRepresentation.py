import mysql.connector 
 
db = mysql.connector.connect(   
	host="127.0.0.1",   
	user="root",   
	password="Bruree06",
	auth_plugin='mysql_native_password',
	database="datarepresentation")
 
 
cursor = db.cursor() 
sql="update student set name= %s, age=%s  where id = %s" 
values = ("Joe",33, 1) 
 
cursor.execute(sql, values) 
 
db.commit() 
print("update done") 