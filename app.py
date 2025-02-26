# a simple script that reformats 1 column of csv data and saves the results in a txt file
results = open('results.txt', 'w')

with open('example_data.csv', 'r') as datafile:
  for line_num, line in enumerate(datafile, 0):
    line = line.replace(' ', '')
    results.write(f'row #{line_num} {line}')

results.close()