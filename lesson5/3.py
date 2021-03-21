### Put file from resources to hdfs (you can read any file from your storage): hadoop fs -copyFromLocal 3.csv hdfs://localhost:9000/
### Execute spark-submit with this file: spark-submit --master local[*] 2.py
### Enjoy))
from pyspark.sql import SparkSession
import pyspark.sql.functions as f
from pyspark.sql.types import StructType, DoubleType, StringType

spark = SparkSession.builder.appName("GeekBrains PySpark").getOrCreate()

schema = StructType() \
    .add("name", StringType(), True) \
    .add("salary", DoubleType(), True)

salaries = spark.read.format("csv")\
    .option("header", True)\
    .schema(schema)\
    .load("hdfs://localhost:9000/3.csv").cache()

salaries.where(f.col('salary') < 20000).show()

avg_salary = salaries.groupBy().avg('salary').collect()[0][0]

print(f"******************************************\n"
      f"Average salary: {avg_salary} "
      f"\n******************************************")
