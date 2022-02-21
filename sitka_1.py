import csv

weather = open('sitka_weather_07-2018_simple.csv','r')

weather_file = csv.reader(weather,delimiter=',')

header_row = next(weather_file)

#print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []

for record in weather_file:
    highs.append(int(record[5]))
print(highs)

import matplotlib.pyplot as plt #giving it an alias

plt.plot(highs,c="red") #highs is the values and c is the color

plt.title("Daily High Temperatures, July 2018", fontsize=16)

plt.xlabel("")
plt.ylabel("Temperatures (F)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

plt.show() #allows you to see the graph

