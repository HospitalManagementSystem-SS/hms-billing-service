import json
import pika
import time
from pika.exceptions import AMQPConnectionError
from app.event_store import store_event_and_generate_invoice


def consume_events():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq", port=5672))
            channel = connection.channel()

            exchange_name = 'appointment_exchange'
            routing_key = 'appointment.created'
            queue_name = 'appointments'

            channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)
            channel.queue_declare(queue=queue_name, durable=True)
            channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

            def callback(ch, method, properties, body):
                event = json.loads(body)
                store_event_and_generate_invoice(event)

            channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
            print("[*] Waiting for messages. To exit press CTRL+C")
            channel.start_consuming()

        except AMQPConnectionError:
            print("[!] RabbitMQ not available, retrying in 10 seconds...")
            time.sleep(10)
