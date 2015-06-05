import csv
import itertools
from sys import argv

script, myinput, myoutput = argv


"""
You need to upload a file with the format 
Title1, Title2, Title3...
Data1.1, Data2.1, Data3.1...
Data1.2, Data2.2, Data3.2...
...

Things to do next:
(1) Write general script for Title1, Title2.
(2) Create pretty interface to do this. (Web app?)
(3) Write script to convert input into corresponding file type.

- Output to Power Editor 

GAH I need to incorporate correspondingi ad name creation.

"""
# Import the csv file. I need to 
reader = csv.reader(open(myoutput, 'rU'))

""" Developing (1)
CategoryLists=[]
CategoryNames = ["AdName", "Title", "Body", "LinkDescription"]
for i in CategoryNames:
	i = []
	CategoryLists.append(i)
"""

#Create arrays for each property
AdName = []
Title = []
Body = []
LinkDescription = []

#Skip header row because I don't want to append that
reader.next()
#Put the data into category lists
for row in reader:
#	AdName.append(row[0])
	Title.append(row[1])
	Body.append(row[2])
	LinkDescription.append(row[3])

# Put the category lists into one array.
iterables = [AdName, Title, Body, LinkDescription]

#Trying to make it easier, instead of writing all the category names manually.
#for i in Categories:
#	Categories[i].append(row[i])

#iterables.append(AdName)
#iterables.append(Title)

# Create output array.
output = [("Adname", "Title", "Body", "LinkDescription")]

#Get iterations.
for t in itertools.product(*iterables):
    output.append(t)
    

print output

# Write result to file
outputfile = open(myoutput, 'wb')
wr = csv.writer(outputfile, quoting=csv.QUOTE_ALL)
wr.writerows(output)

