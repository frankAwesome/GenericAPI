import pika
from flask_restful import Resource, current_app
from flask import jsonify
from sqlalchemy.sql import text

from endpoints.send_to_node import InitMQ
from models.Address import Address
from sql.address import AddressSql


class Rabbit(Resource):
    def get(self):
        response = InitMQ.rpc_request(message='dymanic message borkew', QUEUE_NAME='rpc_queue')

        return response
