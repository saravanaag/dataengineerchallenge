# dataengineerchallenge
dataengineerchallenge

A quick work with python. Please use with python 3.x, I used python 3.7.6 to run and test this.

I have created 4 steps for this.
1. setup the database (used sqlite3), just to be portable whereever you want to test this work quickly.
Basically, step1 is run once step, if you rerun step1 it basically going to reset the database.

2. this is the script which parse through the json file and load all user engagement events. #I have not added any filter rules in this
Step2, can be run as many times as needed. Based on new steams/json files arrive. But run the script only once per file (otherwise duplicates the data for the file which is processed multiple times).

3. prepares the report
Step3, applies the business rule and prepares the report data

4. view the report
Step4, view the report as many times as you wish. Can be run anytime after the database is setup.


############Sample test run############
python step1.dbsetup.py

python step2.eventanalyzer.py data1.json

arguments: ['step2.eventanalyzer.py', 'data1.json'] data1.json
Total rows processed from file: 1000

python step3.preparereport.py

python step4.viewreport.py

(20191230, 31)
(20191231, 33)

python step2.eventanalyzer.py data2.json

arguments: ['step2.eventanalyzer.py', 'data2.json'] data2.json
Total rows processed from file: 1000

python step3.preparereport.py

python step4.viewreport.py

(20191228, 33)
(20191229, 31)
(20191230, 31)
(20191231, 33)

Thanks a lot for reading!
