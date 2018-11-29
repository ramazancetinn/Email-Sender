import pika
import json
import mysql.connector
import time



def create_queue_connection(host, queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    return connection, channel

def publish_message(queue_name, channel, message):
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(message))
    print("Message sent.")


def create_db_connection(host, db_name, user, password):
    connection = mysql.connector.connect(user=user, password=password, host=host, database=db_name)
    return connection

def start(db_host, db_name, db_user, db_password, queue_host, queue_name):

    queue_connection, queue_channel = create_queue_connection(queue_host, queue_name)
    db_connection = create_db_connection(db_host, db_name,db_user, db_password)

    while(True):
        cursor = db_connection.cursor()
        query = ("SELECT *  FROM sendmail_send_mail WHERE status='NEW' limit 10")
        cursor.execute(query)
        for (subject, recipient_list, message) in cursor:
            recipient = recipient_list
            message_send = {'recipient': recipient, 'subject': subject, "body": message}
            publish_message(queue_name, queue_channel, json.dumps(message_send))


        cursor.close()
        time.sleep(10)


    queue_connection.close()
    db_connection.close()



if __name__ == "__main__":
    print('Starting email email sender')
    start(db_host='localhost', db_name='emailsender',db_user='root',db_password='1234',queue_host='localhost',queue_name='selam')