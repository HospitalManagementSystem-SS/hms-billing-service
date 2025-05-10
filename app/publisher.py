import pika
import json

# RabbitMQ connection (adjust host if running remotely)
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Declare the same queue used by the billing service
channel.queue_declare(queue="appointments")

# Sample test event
event = {
    "appointment_id": 101,
    "patient_id": 42,
    "amount": 1200.50  # Simulated total amount
}

# Convert event to JSON and publish it
channel.basic_publish(
    exchange='',
    routing_key='appointments',
    body=json.dumps(event)
)

print(f" [x] Sent appointment event: {event}")
connection.close()
