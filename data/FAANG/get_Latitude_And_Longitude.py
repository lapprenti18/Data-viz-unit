# read values from the file position_of_company.csv
# get the name of the city
# and find an API that will return the latitude and longitude of the city
# save the result in a file called position_of_company_with_coordinates.csv

import csv
from time import sleep
import requests
import asyncio

with open('position_of_company.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    position_of_company = {}
    for row in csv_reader:
        company = row[0]
        city = row[1]
        if company in position_of_company:
            position_of_company[company].append(city)
        else:
            position_of_company[company] = [city]

# remove duplicates
for company in position_of_company:
    position_of_company[company] = list(set(position_of_company[company]))

# print(position_of_company)

with open('position_of_company_with_coordinates.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Company', 'City', 'Latitude', 'Longitude'])
    for company in position_of_company:
        for city in position_of_company[company]:
            print(company, city)
            url = 'http://api.openweathermap.org/geo/1.0/direct?q=' + city + '&appid='

            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                csv_writer.writerow([company, city, data[0]['lat'], data[0]['lon']])
            else:
                print('Error', company, city)
    csv_writer.close(csv_file)
