import csv
import pandas as pd

data = open(r"C:\Users\Dennis Besseling\PycharmProjects\cruise_ship_info.csv")
data = pd.read_csv(data)
print(data)