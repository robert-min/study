from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("streaming_test").getOrCreate()

lines_df = spark.readStream.format("socket").option("host", "localhost").option('port', 9999).load()

words_df = lines_df.select(expr("explode(split(value, ' ')) as word"))
counts_df = words_df.groupby("word").count()

word_count_query = counts_df.writeStream.format("console")\
                            .outputMode("complete")\
                            .option("checkpointLocation", ".checkpoint")\
                            .start()
word_count_query.awaitTermination()