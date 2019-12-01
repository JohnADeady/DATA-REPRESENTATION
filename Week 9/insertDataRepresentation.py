import mysql.connector 
 
db = mysql.connector.connect(   
	host="127.0.0.1",   
	user="root",   
	password="Bruree06",
	auth_plugin='mysql_native_password',
	database="datarepresentation")
 
 
cursor = db.cursor() 
sql="insert into student (name, age) values (%s,%s)" 
values = ("Mary",21) 
 
cursor.execute(sql, values) 
 
db.commit()
print("1 record inserted, ID:", cursor.lastrowid) 