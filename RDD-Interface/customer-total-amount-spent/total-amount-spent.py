# from pyspark import SparkConf, SparkContext

# conf = SparkConf().setMaster("local").setAppName("totalAmountSpent")
# sc = SparkContext(conf = conf)

# # Personal user defined function to parse each line to get (customer_id, amount_spent)
# def parseLine(line):
#     fields = line.split(',')
#     customer_id = int(fields[0])
#     amount_spent = float(fields[2])
#     return (customer_id, amount_spent)

# # Reading the input csv file
# lines = sc.textFile("file:///SparkCourse/customer-total-amount-spent/customer-orders.csv")
# # Parsing each line to get (customer_id, amount_spent)
# rdd = lines.map(parseLine)
# # Computing the total amount spent by each customer
# totalsByCustomerID = rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
# # Collecting the results
# results = totalsByCustomerID.collect()

# # for word in results:
# #     customer_id, inner_tuple = word

# #     item_id, amount_spent = inner_tuple

# #     print(f"{customer_id} :  {amount_spent}")


# for word in results:
#     customer_id = word[0]

#     amount_spent = word[1][0]

#     print(f"{customer_id} :  {amount_spent}")


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Same as getting the total amount spend by each customer but sorting with respect to the total amount spent -----------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# from pyspark import SparkConf, SparkContext

# conf = SparkConf().setMaster("local").setAppName("totalAmountSpent")
# sc = SparkContext(conf = conf)

# def parseLine(line):
#     fields = line.split(',')
#     customer_id = int(fields[0])
#     amount_spent = float(fields[2])
#     return (customer_id, amount_spent)


# lines = sc.textFile("file:///SparkCourse/customer-total-amount-spent/customer-orders.csv")

# rdd = lines.map(parseLine)

# totalsByCustomerID = rdd.mapValues(lambda x: (x, 1)) \
#                         .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

# # Sorting by the total amount spent (which is x[0] from the tuple (amount_spent, count))
# sortedByAmountSpent = totalsByCustomerID.map(lambda x: (x[1][1], x[0])) \
#                                         .sortByKey()

# results = sortedByAmountSpent.collect()

# for amount_spent, customer_id in results:
#     print(f"{customer_id} : {amount_spent}")
#-----------------------------------------------------------------------------------------------------------#

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("totalAmountSpent")
sc = SparkContext(conf = conf)

def parsing(line):
    fields = line.split(',')
    customer_id = fields[0]
    amount_spent = float(fields[2])
    return (customer_id, amount_spent)
    # return (int(fields[0]), float(fields[2]))

lines = sc.textFile("file:///SparkCourse/customer-total-amount-spent/customer-orders.csv")

rdd = lines.map(parsing)

totalsByCustomerID = rdd.reduceByKey(lambda x, y: x + y) 

sortedByAmountSpent = totalsByCustomerID.map(lambda x: (x[1], x[0])).sortByKey()
                                         

results = sortedByAmountSpent.collect();
for result in results:
    customer_id = result[1]
    amount_spent = result[0]
    print(f"{customer_id} : {amount_spent}")

# from pyspark import SparkConf, SparkContext

# conf = SparkConf().setMaster("local").setAppName("SpendByCustomer")
# sc = SparkContext(conf = conf)

# def extractCustomerPricePairs(line):
#     fields = line.split(',')
#     return (int(fields[0]), float(fields[2]))

# input = sc.textFile("file:///SparkCourse/customer-total-amount-spent/customer-orders.csv")
# mappedInput = input.map(extractCustomerPricePairs)
# totalByCustomer = mappedInput.reduceByKey(lambda x, y: x + y)

# results = totalByCustomer.collect();
# for result in results:
#     print(result)