# a simple script that reformats csv data and saves the results in a txt file
import csv

data_file = open ('example_data.csv')
data_reader = csv.reader(data_file)

for row in data_reader:
  rowStr = str(row)
  rowStr = rowStr.replace(' ', '')
  print('row #' + str(data_reader.line_num) + ' ' + rowStr)