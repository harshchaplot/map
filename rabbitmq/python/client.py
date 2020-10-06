#!/usr/bin/env python
import pika
import uuid


class Note(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, req):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(req))
        while self.response is None:
            self.connection.process_data_events()
        return (self.response)


note = Note()

req_type = input("Enter GET or POST\t")
if req_type.lower() == "get":
    id_ip = input("Enter the id\t")
    req = str(req_type) + '*' + str(id_ip)
    response = str(note.call(req))
    response = response[2:]
    response = response[:-1]
    print(response)
elif req_type.lower() == "post":
    title = input("Enter title for the note\t")
    description = input("Enter description for the note\t")
    req = str(req_type) + '*' + str(title) + '*' + str(description)
    response = str(note.call(req))
    response = response[2:]
    response = response[:-1]
    print(response)
    
else:
    print("Enter something valid")



# sudo lsof -i :5672
# telnet localhost 5672