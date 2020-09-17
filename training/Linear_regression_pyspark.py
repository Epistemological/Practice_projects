import pyspark
from pyspark.sql import SparkSession
import csv
import pandas
#SparkSession is now the entry point of Spark
#SparkSession can also be construed as gateway to spark libraries

#create instance of spark class
spark=SparkSession.builder.appName('housing_price_model').getOrCreate()

#create spark dataframe of input csv file
df=pandas.read_csv(r'D:\python coding\pyspark_tutorial\Linear regression\cruise_ship_info.csv')

