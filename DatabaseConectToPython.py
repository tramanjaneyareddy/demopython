import pymysql #this is xammp mysql in phpmyadmin to connect database

con=pymysql.connect(host="localhost",user="root",password="",db="std")
cur=con.cursor()
cur.execute("UPDATE student SET name='ram' WHERE rollno=1 ") #update query
cur.execute("INSERT INTO student(rollno,name) VALUES(4,'king') ") #insert values into table
cur.execute("SELECT * FROM student ") #get or retrieve or fetch value from database
cur.execute(" DELETE FROM student WHERE name='ram' ") #delete from table particluar colum
con.commit() #this step used for update, insert, delete
cur.fetchall()#this step used for get or fetch values
cur.close()
con.close()