from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer


value_schema_str = """
{
   "namespace": "my.test",
   "name": "value",
   "type": "record",
   "fields" : [
     {
       "name" : "name",
       "type" : "string"
     }
   ]
}
"""

key_schema_str = """
{
   "namespace": "my.test",
   "name": "key",
   "type": "record",
   "fields" : [
     {
       "name" : "name",
       "type" : "string"
     }
   ]
}
"""

value_schema = avro.loads(value_schema_str)
key_schema = avro.loads(key_schema_str)
value = {"name": "Shubham Sharma","name": "Amit Jangid","name": "Shubham Jangid",}
key = {"name": "Key"}

avroProducer = AvroProducer({
    'bootstrap.servers': 'localhost:9092',
    'schema.registry.url': 'http://0.0.0.0:8081'
    }, default_key_schema=key_schema, default_value_schema=value_schema)

avroProducer.produce(topic='users', value=value, key=key)
avroProducer.flush()
