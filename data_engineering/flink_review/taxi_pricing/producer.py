import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=["localhost:9092"])

TAXI_TRIPS_TOPIC = "taxi-trips"
with open("./trips/sample_trips.csv", "r") as file:
    next(file)
    for row in file:
        producer.send(TAXI_TRIPS_TOPIC, row.encode("utf-8"))
        print(row)
        time.sleep(1)

producer.flush()