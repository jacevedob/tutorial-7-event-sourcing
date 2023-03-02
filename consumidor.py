import pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('mi-topic', subscription_name='mi-sub')

while True:
    msg = consumer.receive()
    print("Received message: '%s'" % msg.data())
    consumer.acknowledge(msg)

client.close()