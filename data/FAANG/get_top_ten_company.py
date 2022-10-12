import csv

with open('data/Levels_Fyi_Salary_Data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = list(reader)

# count the occurence of each contry
country_count = {}
for row in data:
    country = row[1]
    if country in country_count:
        country_count[country] += 1
    else:
        country_count[country] = 1

country_count = sorted(country_count, key=country_count.get, reverse=True)[:10]
print(country_count)

with open('data/FAANG/TopTenFAANG.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow("timestamp,company,level,title,totalyearlycompensation,location,yearsofexperience,yearsatcompany,tag,basesalary,stockgrantvalue,bonus,gender,otherdetails,cityid,dmaid,rowNumber,Masters_Degree,Bachelors_Degree,Doctorate_Degree,Highschool,Some_College,Race_Asian,Race_White,Race_Two_Or_More,Race_Black,Race_Hispanic,Race,Education")
  for row in data:
    if row[1] in country_count:
      writer.writerow(row)