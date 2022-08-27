import csv
import pandas
"""
temp = []
line = 0
with open("weather_data.csv", "r") as file:
    data = csv.reader(file)
    for row in data:
        if line != 0:
            temp_data = int(row[1])
            temp.append(temp_data)
        line += 1


print(temp)




data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()

length = len(temp_list)

sum_list = sum(temp_list)

answer = sum_list/length

max_val = data["temp"].max()

print(max_val)

print(data[data.temp == max_val])


data = pandas.read_csv("weather_data.csv")
monday = data[data.day == "Monday"]
temp_cel = monday["temp"]


temp_fah = int(temp_cel) * (9/5) + 32
print(temp_fah)
"""

data = pandas.read_csv("centralpark.csv")


dict_Gray = len(data[data["Primary Fur Color"] == "Gray"])
dict_Cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
dict_Black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [dict_Gray, dict_Cinnamon, dict_Black]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("color_count.csv")