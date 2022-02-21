# 1) changing the file to include all the date for the year of 2018
# 2) change the title to "Daily low and high temperatures - 2018
# 3) extract low temps from the file and add to chart
# 4) shade in the area between high and low temperatures

import csv
from datetime import datetime

from matplotlib import dates

weather = open('sitka_weather_2018_simple.csv','r')

weather_file = csv.reader(weather,delimiter=',')

header_row = next(weather_file)

#print(type(header_row))

#for index, column_header in enumerate(header_row):
    #print(index, column_header)

highs = []
lows = []
dates = []

#test_date = datetime.strptime('2018-07-01','%Y-%m-%d') #test for how the datetime.strp function works
#print(test_date)



for record in weather_file:
    highs.append(int(record[5]))
    current_date = datetime.strptime(record[2],'%Y-%m-%d')
    dates.append(current_date)
    lows.append(int(record[6]))


import matplotlib.pyplot as plt #giving it an alias and this is how we create graphs

fig = plt.figure()

plt.plot(dates, highs,c="red") #dates are the x-axis, highs are the y-axis. and c is the color
plt.plot(dates,lows,c="blue")

plt.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)

plt.legend(["High Temps","Low Temps"])


plt.title("Daily Low and High Temperatures, 2018", fontsize=16)

plt.xlabel("Year 2018")
plt.ylabel("Temperatures (F)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

fig.autofmt_xdate()  #makes the dates slanted so we can see the whole thing

plt.show() #allows you to see the graph

plt.subplot(2,1,1)
plt.plot(dates,highs,c="red")
plt.title('Highs')

plt.subplot(2,1,2)
plt.plot(dates,lows,c="blue")
plt.title('Lows')

plt.suptitle("Highs and Lows of Sitka, Alaska 2018")

plt.show()
