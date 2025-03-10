from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.master("local").appName("batch_hw4").getOrCreate()

# Print Spark version
print(f"Spark version: {spark.version}")
