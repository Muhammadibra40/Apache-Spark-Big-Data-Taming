from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.functions import round
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType

spark = SparkSession.builder.appName("TotalSpent").getOrCreate()

schema = StructType([ \
                     StructField("customerID", IntegerType(), True), \
                     StructField("itemID", IntegerType(), True), \
                     StructField("amountSpent", FloatType(), True)])

# // Read the file as dataframe
orders = spark.read.schema(schema).csv("file:///SparkCourse/SparkSQL-On-DataFrames-DataSets/Total-Spent-ByCustomer/customer-orders.csv")


df = orders.select("customerID", "amountSpent")

# df.show()

# df.groupBy("customerID").sum("amountSpent").orderBy("sum(amountSpent)").show()



final_df = df.groupBy("customerID") \
            .sum("amountSpent") \
            .withColumnRenamed("sum(amountSpent)", "total") \
            .withColumn("total", round("total", 2)) \
            .orderBy("total") \

final_df.show(final_df.count())



# df.groupBy("customerID").agg(func.round(sum("amountSpent"), 2)).show()

spark.stop()