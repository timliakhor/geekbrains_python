### Put file from resources to hdfs (you can read any file from your storage): hadoop fs -copyFromLocal 2.txt hdfs://localhost:9000/
### Execute spark-submit with this file: spark-submit --master local[*] 2.py
### Enjoy))
from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.appName("GeekBrains PySpark").getOrCreate()

text = spark.read.text("hdfs://localhost:9000/2.txt").cache()
print(f"******************************************\n"
      f"All rows with blank rows: {text.count()} "
      f"\n******************************************")

text_without_blank_strings = text.filter("value != ''").cache()
print(f"******************************************\n"
      f"All rows without blank rows: {text_without_blank_strings.count()} "
      f"\n******************************************")


words_for_each_string = text_without_blank_strings.withColumn('wordCount', f.size(f.split(f.col('value'), ' ')))
words_for_each_string.show(200)

words_sum = words_for_each_string.groupBy().sum("wordCount").collect()[0][0]

print(f"******************************************\n"
      f"All words in document: {words_sum} "
      f"\n******************************************")

