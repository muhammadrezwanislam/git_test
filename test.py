import csv

with open("test.csv", newline='', encoding ='utf-8')  as g:
	reader = csv.reader(g)
	for row in reader:
		row  = row+row
		print(row)
