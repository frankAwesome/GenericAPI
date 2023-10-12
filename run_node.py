import os
import threading
import pika
import yaml
import importlib
import inspect

from src.yaaylibs import yaay_splash


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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    yaay_splash.yaay_splash()

    module_files = [f for f in os.listdir(os.path.join(script_dir, 'src/nodes')) if f.endswith('.py')]
    imported_classes = {}

    for module_file in module_files:
        module_name = os.path.splitext(module_file)[0]
        module = importlib.import_module(f"{'src.nodes'}.{module_name}")
        classes = [cls for cls in module.__dict__.values() if inspect.isclass(cls)]

        for class_obj in classes:
            class_name = class_obj.__name__
            imported_classes[class_name] = class_obj
            print(f'imported message handler: {class_name}')

    with open(os.path.join(script_dir, 'src/common/queues.yaml'), 'r') as config_file:
        config = yaml.safe_load(config_file)

    workers = []
    for queue_config in config['queues']:
        queue_name = queue_config['name']
        for class_config in config['classes']:
            if class_config['queue'] == queue_name:
                callback_class_name = class_config['name']
                worker = QueueWorker(queue_name, imported_classes[callback_class_name])
                worker.connect()
                workers.append(worker)

    threads = [threading.Thread(target=worker.start_consuming) for worker in workers]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
