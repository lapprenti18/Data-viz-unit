# read Data_Science_Jobs_Salaries1.csv
# count the ocurence of each Contry

import csv

# read Data_Science_Jobs_Salaries1.csv
with open('Data_Science_Jobs_Salaries1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = list(reader)

# count the ocurence of each Contry
country_count = {}
for row in data:
    country = row[7]
    if country in country_count:
        country_count[country] += 1
    else:
        country_count[country] = 1

country_count2 = {}
for row in data:
    country = row[9]
    if country in country_count2:
        country_count2[country] += 1
    else:
        country_count2[country] = 1

country_count = sorted(country_count.items(), key=lambda x: x[1], reverse=True)
country_count2 = sorted(country_count2.items(), key=lambda x: x[1], reverse=True)

# count every country with more than 1 job in country_count or country_count2
country_count3 = {}
for country in country_count:
    if country[1] > 1:
        country_count3[country[0]] = country[1]
for country in country_count2:
    if country[1] > 1:
        if country[0] in country_count3:
            country_count3[country[0]] += country[1]
        else:
            country_count3[country[0]] = country[1]

country_count3 = sorted(country_count3.items(), key=lambda x: x[1], reverse=True)

print(country_count)
# print(country_count2)
# print(len(country_count3))

# print every country not in country_count3


