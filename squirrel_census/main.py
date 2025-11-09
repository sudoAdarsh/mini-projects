import pandas

data = pandas.read_csv("census_data.csv")

count_grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])

count_red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

count_black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [count_grey_squirrels, count_red_squirrels, count_black_squirrels]
}

df = pandas.DataFrame(data=squirrel_dict)

df.to_csv("squirrel_count.csv")