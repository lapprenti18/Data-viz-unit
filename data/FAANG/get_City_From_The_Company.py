# Read all data from TopTenFAANG.csv
# After that save every city for every company and remove duplicates
# in one file position_of_company.csv
# the header will be like this:
# Company, City

import csv

with open('TopTenFAANG.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    position_of_company = {}
    for row in csv_reader:
        company = row[1]
        city = row[5]
        if company in position_of_company:
            position_of_company[company].append(city)
        else:
            position_of_company[company] = [city]
# remove duplicates
for company in position_of_company:
    position_of_company[company] = list(set(position_of_company[company]))

with open('position_of_company.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Company', 'City'])
    print(position_of_company)
    for company in position_of_company:
        for city in position_of_company[company]:
          # I want the city before the first comma in the string
            csv_writer.writerow([company, city[:city.find(',')]])
