from pika import BlockingConnection, ConnectionParameters


connection = BlockingConnection(ConnectionParameters('172.18.0.2'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)
print('[*] Waiting for logs. To exist press CTRL+C')


def callback(ch, methods, properties, body):
    print(f'[x] {body}')


channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)

channel.start_consuming()
