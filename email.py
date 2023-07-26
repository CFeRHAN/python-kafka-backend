import json
import signal
import sys
from kafka import KafkaConsumer

ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"

def stop_consumer(signal, frame):
    print("Stopping Kafka consumer...")
    consumer.close()
    sys.exit(0)

signal.signal(signal.SIGINT, stop_consumer)

consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC, 
    bootstrap_servers="localhost:29092"
)

emails_sent_so_far = set()
print("Gonna start listening")
try:
    for message in consumer:
        consumed_message = json.loads(message.value.decode())
        customer_email = consumed_message["customer_email"]
        print(f"Sending email to {customer_email}")
        emails_sent_so_far.add(customer_email)
        print(f"So far emails sent to {len(emails_sent_so_far)} unique emails")
except KeyboardInterrupt:
    stop_consumer(None, None)
