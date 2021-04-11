from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('json-topic',
                         group_id='app_group',
                         bootstrap_servers=['broker:29092']
                         )
for message in consumer:
    print (message.value)