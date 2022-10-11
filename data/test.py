# read Table_Chart.csv
# convert just the data inside the csv from employment_type,EN,MI,SE,EX to employment_type, experience_level, salary
# write the result to a file

import csv

# read Table_Chart.csv
with open('Table_Chart.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = list(reader)

# convert just the header from employment_type,EN,MI,SE,EX to employment_type, experience_level, salary
header = ['employment_type', 'experience_level', 'salary']
# convert just the data inside the csv from employment_type,EN,MI,SE,EX to employment_type, experience_level, salary
new_row = []

for row in data:
  new_row.append([row[0], 'EN', row[1]])
  new_row.append([row[0], 'MI', row[2]])
  new_row.append([row[0], 'SE', row[3]])
  new_row.append([row[0], 'EX', row[4]])

# write the result to a file
with open('Table_Chart.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in new_row:
        writer.writerow(row)