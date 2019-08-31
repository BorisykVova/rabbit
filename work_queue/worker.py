import time

import pika


def callback(ch, methods, properties, body):
    print(f"[x] Received {body}")
    time.sleep(body.count(b'.'))
    print('[x] Done')
    ch.basic_ack(delivery_tag=methods.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters('172.18.0.2'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
