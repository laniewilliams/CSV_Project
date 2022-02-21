# using the datetime module
# adding dates to the x axis for the month of July 2018

import csv
from datetime import datetime

from matplotlib import dates

weather = open('sitka_weather_07-2018_simple.csv','r')

weather_file = csv.reader(weather,delimiter=',')

header_row = next(weather_file)

#print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []

#test_date = datetime.strptime('2018-07-01','%Y-%m-%d') #test for how the datetime.strp function works
#print(test_date)



for record in weather_file:
    highs.append(int(record[5]))
    current_date = datetime.strptime(record[2],'%Y-%m-%d')
    dates.append(current_date)
print(highs)
print(dates)

import matplotlib.pyplot as plt #giving it an alias and this is how we create graphs

fig = plt.figure()

plt.plot(dates, highs,c="red") #dates are the x-axis, highs are the y-axis. and c is the color



plt.title("Daily High Temperatures, July 2018", fontsize=16)

plt.xlabel("Month of July 2018")
plt.ylabel("Temperatures (F)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

fig.autofmt_xdate()  #makes the dates slanted so we can see the whole thing

plt.show() #allows you to see the graph

