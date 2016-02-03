import os, sys
import csv

directories = []
projectPath = '/repository/download/'+sys.argv[1] #%system.teamcity.projectName%
csvfile = sys.argv[2] #responseTime.csv

#create a list of paths to previous artifacts
for dirname in os.walk(projectPath).next()[1]:
    directories.append(dirname)

#order the list from newest to oldest
directories.reverse() 

print directories
i = 0

#create aggregated CSV file with CSV headers
with open('responseTimeAggregated.csv', 'wb') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["Date", "endpoint", "responseTime"])

for dirPath in directories:
    while i < 10:
        i = i + 1
        with open('responseTime.csv', 'r') as fin, open('/opt/tcagents/tc_cs_agent/temp/agentTmp/responseTimeAggregated.csv', 'w') as fout:
            reader = csv.reader(fin)
            writer = csv.writer(fout)
            for row in reader:
            	try:
            		new_row = row
            		writer.writerow(new_row+[rows[i]])
            		i+=1
            	except IndexError:
            		pass