import csv


#with open('weather_data.csv') as file:
#    csvreader = csv.reader(file)
#    header = next(csvreader)
#    temperatures = [ ]
#    for row in csvreader:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

#with open('weather_data.csv') as data_file:
#    data = data_file.readlines()
#    print(data)

import pandas

#data = pandas.read_csv("weather_data.csv")
##check
#print(type(data))
#print(type(data["temp"]))
#
#data_dict = data.to_dict()
#print(data_dict)
#
#temp_list = data["temp"].to_list()
#print(len(temp_list))

#average = sum(temp_list) / len(temp_list)
#print(average)
#
#print(data["temp"].mean())
#print(data["temp"].max())
#
##get Data in columns
#print(data["condition"])
##another way to work with columns simply by calling data
#print(data.condition)
#
##Get Data row in our dataframe ... Which row ? data[access to row columns + condition]
#print(data[data.day == "Monday" ])
#
#print(data[data.temp == data.temp.max()])
#
#monday = data[data.day == "Monday"]
##we can typing value from a different column
#print(monday.condition)

def celsius_to_fahr(temp_cel):
    """convert fahrenheit to Celsius
    Return input conversion of input"""
    temp_fahrenheit = (temp_cel * 9/5) +32
    return temp_fahrenheit

#print(celsius_to_fahr(monday.temp))

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "james", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("C:/Users/vgiov/Desktop/new_data.csv")