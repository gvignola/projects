import pandas
import pandas as pd
import re

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#use len() like a list for this file iterable
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])#count
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])#count
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])#count
print(gray_squirrel)
print(cinnamon_squirrel)
print(black_squirrel)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count":  [gray_squirrel,cinnamon_squirrel,black_squirrel]
}
df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")