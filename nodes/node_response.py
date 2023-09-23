class NodeResponse:
    @staticmethod
    def send_http_response(response, properties, pika, ch):
        # Send the response back to the response queue
        ch.basic_publish(
            exchange='',
            routing_key=properties.reply_to,
            properties=pika.BasicProperties(
                correlation_id=properties.correlation_id
            ),
            body=str(response)
        )