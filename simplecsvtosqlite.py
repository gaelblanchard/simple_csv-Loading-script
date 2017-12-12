#Quick script to write csv into sqlite database
import csv
import sqlite3

#populate the database
#replace col_name words to reflect the data being inserted
def populate_database(db_name,file_name):
	#Connecting to the sqlite database
	conn = sqlite3.connect(db_name)
	conn.text_factory = str
	c = conn.cursor()
	#creates the table only when it doesnt exist for entry of data from the csv
	c.execute("CREATE TABLE IF NOT EXISTS table_name (col_name TYPE NOT NULL, col_name TYPE NOT NULL, col_name TYPE NOT NULL, col_name TYPE, col_name TYPE, col_name TYPE, col_name TYPE, col_name TYPE, col_name TYPE, col_name TYPE, col_name TYPE, UNIQUE(col_name));") #Create table
	with open(file_name,'rb') as fin:
		dr = csv.DictReader(fin)
		#set i["row_name"] for every column in the csv file
		# n must equal insert or ignore into X (i,..n) == VALUES (?0,...?M)   
		to_db = [(i['col_name'],i['col_name'],i['col_name'],i['col_name'],i['col_name'],i['col_name'],i['col_name'],i['col_name'],i['col_name'],i['col_name'],i['col_name']) for i in dr]

	c.executemany("INSERT OR IGNORE INTO table_name (col_name, col_name,col_name,col_name,col_name,col_name,col_name,col_name,col_name,col_name,col_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
	conn.commit()
	conn.close()


populate_database()