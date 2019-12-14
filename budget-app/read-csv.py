# read a .csv file

import csv

with open('History-100419-033225.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	for row in reader:
		print(row)
		
csvFile.close()
