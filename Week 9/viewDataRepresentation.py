import mysql.connector 
 
db = mysql.connector.connect(   
	host="127.0.0.1",   
	user="root",   
	password="Bruree06",
	auth_plugin='mysql_native_password',
	database="datarepresentation")
 
 
cursor = db.cursor()
sql="select * from student where id = %s" 
values = (1,) 
 
cursor.execute(sql, values) 
result = cursor.fetchall() 
for x in result:   
	print(x) 
 