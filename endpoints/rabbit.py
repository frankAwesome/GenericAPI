import pika
from flask_restful import Resource, current_app
from flask import jsonify
from sqlalchemy.sql import text

from endpoints.send_to_node import InitMQ
from models.Address import Address
from sql.address import AddressSql


class Rabbit(Resource):
    def get(self):
        sql_query = text(AddressSql.GET_ALL)
        result = current_app.db.session.execute(sql_query)
        db_resp = result.fetchall()

        resp = Address(
                city=db_resp[0].city,
                street=db_resp[0].street,
                zip=db_resp[0].zip,
                state=db_resp[0].state
            )

        response = InitMQ.rpc_request(message='dymanic message borkew', QUEUE_NAME='rpc_queue')

        return str(response)

