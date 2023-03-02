#!python
import pulsar

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('my-topic')

for i in range(10):
    producer.send(('Hello-%d' % i).encode('utf-8'))

# Crea un consumidor que recibe los mensajes del topic
consumer = client.subscribe('my-topic')

# Recibe un mensaje del topic
message = consumer.receive()

# Muestra el mensaje
print(message.data())

#client.close()