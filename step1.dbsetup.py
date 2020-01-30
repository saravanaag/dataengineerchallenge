import sqlite3
dbfile = r"database.db"
dbconn = sqlite3.connect(dbfile)
dbcur = dbconn.cursor()
dbcur.execute("drop table IF EXISTS user_engagement_events;")
dbcur.execute("drop table IF EXISTS active_user_table;")
dbcur.execute("create table IF NOT EXISTS user_engagement_events (date DATE not null, engagement_time_msec INTEGER not null);")
dbcur.execute("create table IF NOT EXISTS active_user_table (date DATE not null, active_user_count INTEGER not null);")
dbcur.close()
dbconn.commit()
dbconn.close()