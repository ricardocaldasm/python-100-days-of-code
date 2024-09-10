from csv import reader
import pandas

# with open("day25\weather_data.csv") as weather_file:
#     weather_data = weather_file.readlines()
#     print(weather_data)

# with open("day25\weather_data.csv") as weather_file:
#     weather_data = reader(weather_file)  # created an object
#     temperatures = list()
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pandas.read_csv(r"day25\weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

mean_temp = data["temp"].mean()
print(mean_temp)

print(data["condition"])  # same as below
print(data.condition)  # pandas converts heading into attributes

# get data in row
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

# create a dataframe from scratch
data_dict2 = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
data2 = pandas.DataFrame(data_dict2)
print(data2)
data2.to_csv(r"day25\new_data2.csv")