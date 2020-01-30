import json
import sqlite3
import sys
try:
	print('arguments:', str(sys.argv),str(sys.argv[1])) #expects one argument, input file name
	inputfile = str(sys.argv[1])
	dbfile = r"database.db"
	dbconn = sqlite3.connect(dbfile)
	dbcur = dbconn.cursor()
	rownumber = 0
	with open(inputfile, 'r') as file:
		for row in file:
			event = json.loads(row)
			event_params = event["event_params"]
			if event["event_name"] == "user_engagement":
				for key in event_params:
					if key["key"] == 'engagement_time_msec': #and int(key["value"]["int_value"]) >= 3000:
						dbcur.execute("insert into user_engagement_events values("+event["event_date"]+","+key["value"]["int_value"]+");")
			rownumber += 1
	print("Total rows processed from file:", rownumber)
	dbcur.close()
	dbconn.commit()
	dbconn.close()
except:
	print("sorry, something went wrong")