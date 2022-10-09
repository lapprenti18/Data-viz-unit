# read Data_Science_Jobs_Salaries1.csv
# calculate average, min, max salary per country
# print the result

import csv

# read Data_Science_Jobs_Salaries1.csv
with open('Data-viz-unit/data/Data_Science_Jobs_Salaries1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = list(reader)

# calculate average, min, max salary per country
country_salary = {}
for row in data:
    country = row[9]
    salary = int(row[6])
    if country in country_salary:
        country_salary[country].append(salary)
    else:
        country_salary[country] = [salary]

# print the result
for country, salary in country_salary.items():
    print(country, min(salary), max(salary), sum(salary)/len(salary))


# write the result to a file
with open('Data-viz-unit/data/earn_per_contry.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['country', 'min', 'max', 'average'])
    for country, salary in country_salary.items():
        writer.writerow([country, min(salary), max(salary), "{:.0f}".format(sum(salary)/len(salary))])
        