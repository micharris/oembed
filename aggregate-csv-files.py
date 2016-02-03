import os, sys
import csv

directories = []
csvRows = []
projectPath = '/repository/download/'+sys.argv[1] #%system.teamcity.projectName%
csvfile = sys.argv[2] #responseTime.csv

#create a list of paths to previous artifacts
for dirname in os.walk(projectPath).next()[1]:
    directories.append(dirname)
    print dirname

#order the list from newest to oldest
directories.reverse() 

i = 0

#read all previous csv files and add rows to list
for dirPath in directories:
    while i < 10:
        i = i + 1
        with open(projectPath+dirPath+csvfile, 'r') as fin:
            reader = csv.reader(fin)
            for row in reader:
            	try:
                    csvRows.append(row)
            	except IndexError:
            		pass

#create aggregated CSV file
with open('/opt/tcagents/linuxtcagent/temp/agentTmp/responseTimeAggregated.csv', 'wb') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["Date", "endpoint", "responseTime"])
    for row in csvRows:
        writer.writerow(row)