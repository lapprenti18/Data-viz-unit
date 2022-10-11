# I want the mean salary for each experience level for each employment type
# I will read the data from the Data_Science_Jobs_Salaries1.csv file
# I will write the data to the Table_Chart.csv file
# and all missing values to be the one from the previous row
# and if there is 3 or more missing values in a row, then skip that row

import csv
import statistics

# read Data_Science_Jobs_Salaries1.csv
with open('./Data_Science_Jobs_Salaries1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = list(reader)

# calculate average salary per employment type and experience level
employment_type_experience_salary = {}
for row in data:
    employment_type = row[3]
    experience = row[1]
    salary = int(row[6])
    if employment_type in employment_type_experience_salary:
        if experience in employment_type_experience_salary[employment_type]:
            employment_type_experience_salary[employment_type][experience].append(salary)
        else:
            employment_type_experience_salary[employment_type][experience] = [salary]
    else:
        employment_type_experience_salary[employment_type] = {experience: [salary]}
# print(employment_type_experience_salary)

# write the result to a file
with open('./Table_Chart.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['employment_type', 'EN', 'MI', 'SE', 'EX'])
    for employment_type, experience_salary in employment_type_experience_salary.items():
        row = [employment_type]
        for experience in ['EN', 'MI', 'SE', 'EX']:
            if experience in experience_salary:
                row.append("{:.0f}".format(statistics.mean(experience_salary[experience])))
            else:
              if len(row) > 1:
                  row.append(row[-1])
              else:
                  row.append(0)
        writer.writerow(row)