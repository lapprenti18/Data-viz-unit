# read TopTenFAANG.csv and if the company name is in the line, write append it to the file with the company name

import csv

with open('TopTenFAANG.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        if line[1] == 'company':
            continue
        with open(line[1] + '.csv', 'a') as f:
            f.write(','.join(line) + '\n')

