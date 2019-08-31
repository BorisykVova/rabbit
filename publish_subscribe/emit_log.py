import sys

from pika import BlockingConnection, ConnectionParameters


connection = BlockingConnection(ConnectionParameters('172.18.0.2'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or 'info: Hello Word!'
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(f'[x] Send {message}')
connection.close()
