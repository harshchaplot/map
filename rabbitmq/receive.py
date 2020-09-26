import pika, sys, os, json, string, random

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='MyQueue8')

    notes = {}
    letters = string.ascii_lowercase
    letters += "0123456789!@#$%^&*()"

    def callback(ch, method, properties, body):
        output = str(body)
        output = output[2:]
        output = output[:-1]
        output = list(output)
        for i in range(len(output)):
            if output[i] == '\'':
                output[i] = '\"'
        output = "".join(output)
        output = json.loads(output)
        try:
            find_id = output['id']
            print("Note with id ",find_id)
            print(notes[find_id])
        except:
            post_id = ''.join(random.choice(letters) for i in range(8))
            notes[post_id] = output
            print(notes)

    channel.basic_consume(queue='MyQueue8', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)