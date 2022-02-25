from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
producer.send("example-source", b"test kafka to kafka")
producer.flush()