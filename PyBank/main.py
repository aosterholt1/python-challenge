import os 
import csv

csvpath = os.path.join("/Users/aosmacbookpro/Desktop/gitlab-data-analytics/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")
	
with open(csvpath, newline= '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ",")
	csv_header = next(csvfile)
	value = len(list(csvreader))
	print (value)
	
	for row in csvreader:
		print(value)