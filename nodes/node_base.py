class RabbitMQWorkerCallbackBase:
    def callback(self, ch, method, properties, body):
        raise NotImplementedError("Subclasses must implement the callback method.")