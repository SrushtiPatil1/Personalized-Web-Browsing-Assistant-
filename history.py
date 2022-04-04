import os
import sqlite3
import csv  
con  = sqlite3.connect('C:/Users/SRUSHTI/AppData/Local/Google/Chrome/User Data/Default/History')
cur = con.cursor()
#cur.execute("create table history(url, title, visit_count, last_visit_time)")
cur.execute("select url, title, visit_count, last_visit_time from urls")
results = cur.fetchall()
rows = []
for result in results:
     print(result)
     rows.append(result) 
     fields = ['url', 'title', 'visit_count', 'last_visit_time']  
     filename = "history_analysis.csv" 
    
with open(filename, 'w') as csvfile:   
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)   
    csvwriter.writerows(rows)





