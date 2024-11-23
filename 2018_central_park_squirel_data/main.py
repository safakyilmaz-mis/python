import pandas
import os

current_dir = os.path.dirname(__file__)
input_file = os.path.join(current_dir, "2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240524.csv")
output_file = os.path.join(current_dir, "Squirrel Count.csv")

datas = pandas.read_csv(input_file)
datasToList = datas["Primary Fur Color"].tolist()

blackColor = datasToList.count("Black")
grayColor = datasToList.count("Gray")
cinnamonColor = datasToList.count("Cinnamon")

SqColor = {"Squirrel Color": ["Gray", "Black", "Cinnamon"],
           "Count": [grayColor, blackColor, cinnamonColor]}
pandas.DataFrame(SqColor).to_csv(output_file)
