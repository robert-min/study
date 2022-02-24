from kafka import KafkaConsumer, KafkaProducer
import json

# Kafka Topic
PAYMENT_TOPIC = "payments"
FRAUD_TOPIC = "fraud_payments"
LEGIT_TOPIC = "legit_payments"

brokers = ["localhost:9091", "localhost:9092", "localhost:9093"]

consumer = KafkaConsumer(PAYMENT_TOPIC, bootstrap_servers=brokers)
producer = KafkaProducer(bootstrap_servers=brokers)

# PAYMENT_TYPE = BITCOIN 구분
def is_suspicious(transactions):
    if transactions["PAYMENT_TYPE"] == "BITCOIN":
        return True
    return False

for message in consumer:
    msg = json.loads(message.value.decode())
    topic = FRAUD_TOPIC if is_suspicious(msg) else LEGIT_TOPIC
    producer.send(topic, json.dumps(msg).encode("utf-8"))
    print(topic, is_suspicious(msg), msg["PAYMENT_TYPE"])