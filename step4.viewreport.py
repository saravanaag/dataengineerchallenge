import sqlite3
dbfile = r"database.db"
dbconn = sqlite3.connect(dbfile)
dbcur = dbconn.cursor()
dbcur.execute("select * from active_user_table order by date;")
rows = dbcur.fetchall()
for row in rows:
	print(row)
dbcur.close()
dbconn.close()