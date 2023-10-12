from flask_restful import Resource

from src.yaaylibs.send_to_node import InitMQ


class Rabbit(Resource):
    def get(self):
        response = InitMQ.rpc_request(message='dymanic message borkew', QUEUE_NAME='rpc_queue')

        return response
