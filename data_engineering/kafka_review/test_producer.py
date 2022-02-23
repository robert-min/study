from kafka import KafkaProducer

# broker 지정(도커 카프카 컨테이너로 지정한 포터로)
brokers = ["localhost:9091", "localhost:9092", "localhost:9093"]
topicName = "test-topic"

producer = KafkaProducer(bootstrap_servers = brokers)

producer.send(topicName, b"test message")
producer.flush()