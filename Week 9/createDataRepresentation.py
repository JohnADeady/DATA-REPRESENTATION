import mysql.connector 
 
mydb = mysql.connector.connect(   
	host="127.0.0.1",   
	user="root",   
	password="Bruree06",
	auth_plugin='mysql_native_password',
	database="datarepresentation")
 
 
mycursor = mydb.cursor() 

sql="CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)" 
 
 
mycursor.execute(sql) 