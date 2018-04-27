from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError

c = AvroConsumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test-consumer-group',
    'schema.registry.url': 'http://0.0.0.0:8081'})

c.subscribe(['users'])

while True:
    try:
        msg = c.poll(10)

    except SerializerError as e:
        print("Message deserialization failed for {}: {}".format(msg, e))
        break

    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    print(msg.value())

c.close()
