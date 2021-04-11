How to test this:

Clone the repository.

Edit docker-compose.yml with the following environment variables, you can find them in your User Settings, in “send your logs”, select Docker from the left panel and you will see them in the example.

PRIVATE_KEY   <--- this is Coralogix user private key.
COMPANY_ID <--- this is Coralogix company ID.


docker-compose build

docker-compose up 

You can access Kafka Management UI  accessing http://localhost:9021

Once the UI is up, and Kafka cluster is stable.

You can use this curl example to make the POST request:

curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
"message" : "This is the test message"
}' \
 'http://localhost:5000'

If everything is ok,  you should be able to see both API and Consumer logs in Coralogix Dashboard.
