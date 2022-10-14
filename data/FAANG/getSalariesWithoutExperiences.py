# I want to get the min, average, max salary for each employment type
# I will read the data from the TopTenFAANG.csv file
import csv
import math

titles = {
  "Software Engineer": {},
  "Product Manager": {},
  "Data Scientist": {},
  "Product Designer": {},
  "Hardware Engineer": {},
  "Solution Architect": {},
  "Technical Program Manager": {},
  "Mechanical Engineer": {},
  "Business Analyst": {},
  "Human Resources": {},
  "Marketing": {},
  "Software Engineering Manager": {},
  "Sales": {},
  "Management Consultant": {},
}

with open('TopTenFAANG.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # skip header
    for row in csv_reader:
        title = row[3]

        if row[6] == '0':
            salary = int(row[4])
            if title in titles:
                if salary in titles[title]:
                    titles[title][salary] += 1
                else:
                    titles[title][salary] = 1
            else:
                titles[title] = {salary: 1}

for title in titles:
    total = 0
    min_salary = 0
    max_salary = 0
    for salary in titles[title]:
        total += salary * titles[title][salary]
        if min_salary == 0 or salary < min_salary:
            min_salary = salary
        if max_salary == 0 or salary > max_salary:
            max_salary = salary
    average = total / sum(titles[title].values())
    print('Title: {0} - Min: {1} - Average: {2} - Max: {3}'.format(title, min_salary, int(average), max_salary))

# write the data to a file
with open('salariesWithoutExperiences.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'Min', 'Average', 'Max'])
    for title in titles:
        total = 0
        min_salary = 0
        max_salary = 0
        for salary in titles[title]:
            total += salary * titles[title][salary]
            if min_salary == 0 or salary < min_salary:
                min_salary = salary
            if max_salary == 0 or salary > max_salary:
                max_salary = salary
        average = total / sum(titles[title].values())
        csv_writer.writerow([title, min_salary, int(average), max_salary])