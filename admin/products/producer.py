import pika

params = pika.URLParameters('amqps://quzzhwzf:GasqFvGyINTMleDwX_LtwBlf8DY84tYp@puffin.rmq2.cloudamqp.com/quzzhwzf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')
