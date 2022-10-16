# read Data_Science_Jobs_Salaries1.csv
# calculate average, min, max salary per employment type
# write the result to a file

import csv

# read Data_Science_Jobs_Salaries1.csv
with open('Data-viz-unit/data/FAANG/TopTenFAANG.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = list(reader)

# calculate average, min, max salary per employment type
employment_type_salary = {}
for row in data:
    employment_type = row[3]
    salary = int(row[4])
    if salary < 0:
        continue
    if employment_type in employment_type_salary:
        employment_type_salary[employment_type].append(salary)
    else:
        employment_type_salary[employment_type] = [salary]

# write the result to a file
with open('Data-viz-unit/data/employment_type_salary.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['employment_type', 'min', 'max', 'average'])
    for employment_type, salary in employment_type_salary.items():
        writer.writerow([employment_type, min(salary), max(salary), "{:.0f}".format(sum(salary)/len(salary))])