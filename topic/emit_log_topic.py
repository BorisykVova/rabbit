import sys

from pika import BlockingConnection, ConnectionParameters


connection = BlockingConnection(ConnectionParameters('172.18.0.2'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello Word!'

channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)

print(f'[x] Sent {routing_key}:{message}')
connection.close()
