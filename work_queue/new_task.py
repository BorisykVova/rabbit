import sys

from pika import BlockingConnection, ConnectionParameters, BasicProperties


connection = BlockingConnection(ConnectionParameters('172.18.0.2'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello World!'
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=BasicProperties(delivery_mode=2))

print(f'[x] Sent {message}')

connection.close()