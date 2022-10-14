# I want to get the salary of the first 10 years of experience of each company
# I want the 10 values of the salary of each company with the average of for each year per company
# in the FAANG companies and save it in different csv file

import csv

companies = ['Amazon.csv', 'Apple.csv', 'Facebook.csv', 'Google.csv', 'Cisco.csv', 'IBM.csv', 'Intel.csv', 'Microsoft.csv', 'Oracle.csv', 'Salesforce.csv']

for company in companies:
    data = [{ 'salary': 0, 'count': 0} for k in range(10)]
    print(data)
    with open('../'+company, 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
          if (row[7].isnumeric() == False or row[3] != "Software Engineer"):
            continue
          year = int(row[7])
          if (year < 10):
            data[year]['salary'] += int(row[4])
            data[year]['count'] += 1
    csvFile.close()
    with open('firstTenYears'+company, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['year', 'salary'])
        for i in range(10):
            writer.writerow([i, round(data[i]['salary']/data[i]['count'])])
    csvFile.close()
