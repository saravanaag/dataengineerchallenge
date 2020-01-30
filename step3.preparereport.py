import sqlite3
dbfile = r"database.db"
dbconn = sqlite3.connect(dbfile)
dbcur = dbconn.cursor()
dbcur.execute("insert into active_user_table select date,count(*) from user_engagement_events where engagement_time_msec >= 3000 group by date;")
dbcur.execute("delete from user_engagement_events;")
dbcur.close()
dbconn.commit()
dbconn.close()