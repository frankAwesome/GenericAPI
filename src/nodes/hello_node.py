import pika

from src.yaaylibs.node_base import RabbitMQWorkerCallbackBase
from src.yaaylibs.node_response import NodeResponse


class YourCallbackClass1(RabbitMQWorkerCallbackBase):
    def callback(self, ch, method, properties, body):
        # Implement your specific callback logic here
        response = f"Callback 1 received"
        print(response)

        NodeResponse.send_http_response(response=response, pika=pika, properties=properties, ch=ch, method=method)