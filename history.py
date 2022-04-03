import os
import sqlite3
import csv  
con  = sqlite3.connect('C:/Users/SRUSHTI/AppData/Local/Google/Chrome/User Data/Default/History')
cur = con.cursor()
#cur.execute("create table history(url, title, visit_count, last_visit_time)")
cur.execute("select url, title, visit_count, last_visit_time from urls")
results = cur.fetchall()
rows = []

def parse(url):
	try:
		parsed_url_components = url.split('//')
		sublevel_split = parsed_url_components[1].split('/', 1)
		domain = sublevel_split[0].replace("www.", "")
		return domain
	except IndexError:
		print ("URL format error!")


for result in results:
     def parse(url):
          parsed_url_components = url.split('//')
          sublevel_split = parsed_url_components[1].split('/', 1)
          domain = sublevel_split[0].replace("www.", "")
          return domain

     sites_count = {} #dict makes iterations easier :D

     for url, count in results:
          url = parse(url)
          if url in sites_count:
               sites_count[url] += 1
          else:
               sites_count[url] = 1
	     

     print(result)
     rows.append(result) 
     fields = ['url', 'title', 'visit_count', 'last_visit_time']  
     filename = "history_analysis.csv" 
    
with open(filename, 'w') as csvfile:   
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)   
    csvwriter.writerows(rows)





