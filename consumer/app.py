from kafka import KafkaConsumer
import json

print('linea print')


# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('json-topic',
                         group_id='app_group',
                         bootstrap_servers=['broker:29092']
                         )
#print ('antes del for')
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    #print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                      message.offset, message.key,
    #         
    #))
    #print ('adentrodelfor')
    print (message.value)



print ('fuera del for')                                     
# consume json messages
#KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))
