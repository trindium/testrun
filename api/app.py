from flask import Flask, request, jsonify
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
from datetime import datetime

#import logging
#logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['POST'])
def home():
    data = request.json
    data.update({'timestamp' : str(datetime.now())})
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))
    producer.send('json-topic', data)
    return jsonify(data)



app.run(host="localhost", port=8000)
