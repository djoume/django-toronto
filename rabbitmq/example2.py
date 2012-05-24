import pika

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
    pika.log.info('Exchange declared')


if __name__ == '__main__':
    parameters = pika.ConnectionParameters('127.0.0.1')
    connection = pika.adapters.SelectConnection(parameters, on_connected)
    try:
        connection.ioloop.start()
    except KeyboardInterrupt:
        connection.close()
        connection.ioloop.start()
