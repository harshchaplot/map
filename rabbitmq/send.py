import pika, json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='MyQueue8')

req = input("Enter GET or POST\t")
if req.lower() == "get":
	note = {}
	note['id'] = input("Enter the id of the note you want\t")
	note = json.dumps(note)
	channel.basic_publish(exchange='', routing_key='MyQueue8', body=note)
	print("GET request sent")
	connection.close()

elif req.lower() == "post":
	note = {}
	note['title'] = input("Enter title for the note\t")
	note['description'] = input("Enter description for the note\t")
	note = json.dumps(note)
	channel.basic_publish(exchange='', routing_key='MyQueue8', body=note)
	print("POST request sent")
	connection.close()

else:
	print("Invalid response")
	connection.close()