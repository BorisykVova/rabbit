import pika


def callback(ch, methods, properties, body):
    print(f"[x] Received {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters('172.18.0.2'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
