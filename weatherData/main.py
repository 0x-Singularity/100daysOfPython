import csv
import pandas 

#with open("weatherData/weather_data.csv") as data_file:
    #data = csv.reader(data_file)
   # temperatures = []
    #for row in data:
        #if row[1] != "temp":
            #temperatures.append(int(row[1]))
  
        
data = pandas.read_csv("weatherData/weather_data.csv")
data_dict = data.to_dict()
temperature_list = data["temp"].to_list()

max = data["temp"].max()

print(max)

totalNumber = 0
tempListLength = len(temperature_list)

for temp in temperature_list:
    totalNumber += temp

temp_average = totalNumber / tempListLength

print(temp_average)


