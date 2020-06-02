from bs4 import BeautifulSoup as BS
from urllib.request import Request,urlopen
import psycopg2
import time
import matplotlib.pyplot  as plt
import matplotlib

import urllib.request
# tsa website
url = 'https://www.tsa.gov/coronavirus/passenger-throughput'
req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
response = urlopen(req, timeout=20).read()

# set variables
totalData = []
values2019 = []
values2020 = []
dates = []
days = []

time.sleep(.3)
soup = BS(response, 'html.parser')
time.sleep(.3)
data = soup.findAll('td')
# parse text in total data
for each in data:
    b = each.text.strip()
    bb = b.replace(",","")
    totalData.append(bb)

# dates = summation n = 0 to n = 282, 3*n
for i in range(len(totalData)):
    try:
        ndates = i*3
        dates.append(totalData[ndates])
    except:
        pass
# values2019 = summation n = 1 to n = 282, (n + (n-1)*2)
for i in range(len(totalData)):
    try:
        if i == 0:
            pass
        else:
            n2019 = i + (i-1)*2
            values2019.append(int(totalData[n2019]))
    except:
        pass

# values2020 = summation n = 0 to n = 282, (n + (n+1)*2)
for i in range(len(totalData)):
    try:
        if i == 0:
            pass
        else:
            n2020 = i + (i+1)*2
            values2020.append(int(totalData[n2020]))
    except:
        pass
for i in range(len(values2019)):
    days.append(i)
values2019.reverse()
dates.reverse()
values2020.reverse()

plt.figure('TSA Plot')
plt.subplot(211)
plt.plot(days,values2019)
plt.plot(days,values2020)
plt.title('TSA Checkpoint Travel Numbers for 2020 and 2019')
plt.legend(['2020','2019'])
plt.ylabel('Total Traveler')
plt.grid()

plt.subplot(212)
plt.plot(days,values2019)
plt.plot(days,values2020)
plt.yscale('log')
plt.legend(['2020','2019'])
plt.ylabel('Total Traveler')
plt.xlabel('Days [March 1st - Current]')
plt.grid()
plt.show()
print("Data read successfully")
