# 1) changing the file to include all the date for the year of 2018
# 2) change the title to "Daily low and high temperatures - 2018
# 3) extract low temps from the file and add to chart
# 4) shade in the area between high and low temperatures

import csv
from datetime import datetime

from matplotlib import dates

d_weather = open('death_valley_2018_simple.csv','r')

d_weather_file = csv.reader(d_weather,delimiter=',')

header_row = next(d_weather_file)


for index, column_header in enumerate(header_row):
    if column_header == 'TMIN':
        d_tmin = index
    if column_header == 'TMAX':
        d_tmax = index
    if column_header == 'NAME':
        d_name_ind = index


d_highs= []
d_lows = []
d_dates = []


for record in d_weather_file:

    try:
        current_date = datetime.strptime(record[2],'%Y-%m-%d')
        high = int(record[d_tmax])
        low = int(record[d_tmin])
        d_name = record[d_name_ind]
        
        

    except ValueError:
        print(f'Missing data for {current_date}')


    else:
        d_highs.append(high)
        d_dates.append(current_date)
        d_lows.append(low)

#FOR SITKA WEATHER ------------------------------------------------------------

s_weather = open('sitka_weather_2018_simple.csv','r')

s_weather_file = csv.reader(s_weather,delimiter=',')

header_row = next(s_weather_file)


for index, column_header in enumerate(header_row):
    if column_header == 'TMIN':
        s_tmin = index
    if column_header == 'TMAX':
        s_tmax = index
    if column_header == 'NAME':
        s_name_ind = index

s_highs= []
s_lows = []
s_dates = []


for record in s_weather_file:
    try:
        current_date = datetime.strptime(record[2],'%Y-%m-%d')
        high = int(record[s_tmax])
        low = int(record[s_tmin])
        s_name = record[s_name_ind]

    except ValueError:
        print(f'Missing data for {current_date}')


    else:
        s_highs.append(high)
        s_dates.append(current_date)
        s_lows.append(low)




import matplotlib.pyplot as plt #giving it an alias and this is how we create graphs

fig = plt.figure()

plt.subplot(2,1,1)
plt.plot(s_dates,s_highs,c="red")
plt.plot(s_dates,s_lows,c="blue")
plt.fill_between(s_dates,s_highs,s_lows,facecolor="blue",alpha=0.1)
plt.title(s_name)

plt.subplot(2,1,2)
plt.plot(d_dates,d_highs,c="red")
plt.plot(d_dates,d_lows,c="blue")
plt.fill_between(d_dates,d_highs,d_lows,facecolor="blue",alpha=0.1)
plt.title(d_name)

plt.suptitle("Temperature comparison between "+s_name+" and "+d_name, fontsize=16)

#plt.tick_params(axis="both",which="major",labelsize=16)

fig.autofmt_xdate()  #makes the dates slanted so we can see the whole thing

plt.show()
