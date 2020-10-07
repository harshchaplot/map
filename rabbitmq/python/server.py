#!/usr/bin/env python
import pika, string, random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='MYQUEUE')

letters = string.ascii_lowercase
letters += "0123456789!@#$%^&()"
note = {}
note['00000000'] = {'id':'00000000', 'title':'This is a sample note', 'description':'Lorem ipsum'}


def on_request(ch, method, props, body):
    req = str(body)
    req = req[2:]
    req = req[:-1]
    req = req.split('*')
    if req[0].lower() == "get":
        find_id = req[1]
        response = note[find_id]
    elif req[0].lower() == "post":
        insert_id = ''.join(random.choice(letters) for i in range(8))
        my_note = {}
        my_note['id'] = insert_id
        my_note['title'] = req[1]
        my_note['description'] = req[2]
        note[insert_id] = my_note
        response = "Note inserted"
    else:
        response = "Error"

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Response sent")
    for x,y in note.items():
        print('ID: ', x, '\t', y)
        print('_______________________________________________________________________________')
    print('x-----------------------------------------------------------------------------x')


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='MYQUEUE', on_message_callback=on_request)

print("Awaiting requests")
channel.start_consuming()
