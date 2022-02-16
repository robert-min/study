# 패키지
import pandas as pd
from pyspark import SparkConf, SparkContext

# Spark 설정
conf = SparkConf().setMaster("local").setAppName("pyspark_test")
sc = SparkContext(conf=conf)

# 데이터 로드
directory = "/Users/robertmin/PycharmProjects/study/data_engineering/spark_review/data"
filename = "tripdata_2020-03.csv"

# 데이터 파싱
lines = sc.textFile(f"file:///{directory}/{filename}")
header = lines.first()
filtered_lines = lines.filter(lambda row:row != header)

# 원하는 데이터 추출
dates = filtered_lines.map(lambda x: x.split(",")[3].split(" ")[0])
result = dates.countByValue()

# CSV로 결과 저장
pd.Series(result, name='trips').to_csv("trip_data.csv")