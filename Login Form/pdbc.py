#program to establish the connection
import mysql.connector
host = 'localhost'
user ='root'
pswd='1996shubu'
database = 'login_page'
port = '3306'
password_lst=[]
username_lst=[]

def read_record():
	try:
		#establishing connection to database
		my_con = mysql.connector.connect(host=host,user=user,password=pswd,database=database,port=port)

		#creation of a cursor object which is pointing towards the table
		my_cursor = my_con.cursor()

		#write query
		sql_query ="""select username,password from information"""

		#execution of sql query	
		my_cursor.execute(sql_query)

		
		record = my_cursor.fetchall()
		for (username,password) in record:
			username_lst.append(username)
			password_lst.append(password)

		return(password_lst)
		return(username_lst)		
	except Exception as e:
		raise e

	finally:
		my_con.close()


if __name__=="__main__":
	read_record()
	print(password_lst)