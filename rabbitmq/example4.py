import pika
import sys
import time

pika.log.setup(color=True)

connection = None
channel = None


def on_connected(connection):
    pika.log.info('Connected to the Rabbit!')
    connection.channel(on_channel_open)


def on_channel_open(channel_):
    global channel
    channel = channel_
    pika.log.info('Received our Channel')
    channel.exchange_declare(exchange='LunchAndLearn',
        type='direct', durable=False, auto_delete=False,
        callback=on_exchange_declared)


def on_exchange_declared(frame):
    pika.log.info('Exchange declared.')
    channel.queue_declare(queue='learn', durable=False,
        exclusive=False, auto_delete=False,
        callback=on_queue_declared)


def on_queue_declared(frame):
    pika.log.info('Queue declared.')
    channel.queue_bind(exchange='LunchAndLearn', queue='learn',
        routing_key='learn', callback=on_binding)


def on_binding(frame):
    pika.log.info('Binding done.')
    channel.basic_consume(on_message, queue='learn')


def on_message(ch, method, properties, body):
    print 'Learning %s' % ''.join(body.split()[1:]),
    sys.stdout.flush()
    for i in range(3):
        time.sleep(1)
        print '.',
        sys.stdout.flush()
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print 'DONE'


if __name__ == '__main__':
    parameters = pika.ConnectionParameters('127.0.0.1')
    connection = pika.adapters.SelectConnection(parameters, on_connected)
    try:
        connection.ioloop.start()
    except KeyboardInterrupt:
        connection.close()
        connection.ioloop.start()
