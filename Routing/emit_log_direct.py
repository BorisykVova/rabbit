import sys

from pika import BlockingConnection, ConnectionParameters


connection = BlockingConnection(ConnectionParameters('172.18.0.2'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv[1]) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello Word!'

channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

print(f'[x] Sent {severity}:{message}')
connection.close()
