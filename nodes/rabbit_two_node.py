import pika
from nodes.node_base import RabbitMQWorkerCallbackBase
from nodes.node_response import NodeResponse


class YourCallbackClass2(RabbitMQWorkerCallbackBase):
    def callback(self, ch, method, properties, body):
        # Implement your specific callback logic here
        response = f"Fuck yea yea: {body}"
        print(response)

        NodeResponse.send_http_response(response=response, pika=pika, properties=properties, ch=ch)
