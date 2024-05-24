import pandas

datas = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240524.csv")
datasToList = datas["Primary Fur Color"].tolist()

blackColor = datasToList.count("Black")
grayColor = datasToList.count("Gray")
cinnamonColor = datasToList.count("Cinnamon")

SqColor = {"Squirrel Color": ["Gray", "Black", "Cinnamon"],
           "Count": [grayColor, blackColor, cinnamonColor]}
pandas.DataFrame(SqColor).to_csv("Squirrel Count.csv")
