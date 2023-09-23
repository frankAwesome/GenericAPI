import threading

import pika

from nodes.hello_node import YourCallbackClass1
from nodes.rabbit_two_node import YourCallbackClass2


class RabbitMQWorkerCallbackBase:
    def callback(self, ch, method, properties, body):
        raise NotImplementedError("Subclasses must implement the callback method.")


class QueueWorker:
    def __init__(self, queue_name, callback_class):
        self.queue_name = queue_name
        self.callback_class = callback_class
        self.connection = None
        self.channel = None

    def connect(self, host='localhost'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback)

    def callback(self, ch, method, properties, body):
        callback_instance = self.callback_class()
        callback_instance.callback(ch, method, properties, body)

    def start_consuming(self):
        print(f'Worker for queue "{self.queue_name}" is waiting for RPC requests. To exit, press Ctrl+C')
        self.channel.start_consuming()

if __name__ == '__main__':
    queues_and_callbacks = [
        {'queue_name': 'rpc_queue', 'callback_class': YourCallbackClass1},
        {'queue_name': 'rpc_queue_2', 'callback_class': YourCallbackClass2},
        # Add more queue/callback pairs as needed
    ]

    workers = []
    for item in queues_and_callbacks:
        worker = QueueWorker(item['queue_name'], item['callback_class'])
        worker.connect()
        workers.append(worker)

    # Start each worker in a separate thread
    threads = [threading.Thread(target=worker.start_consuming) for worker in workers]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
