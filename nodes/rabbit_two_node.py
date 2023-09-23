import json

import pika
from flask import jsonify
from sqlalchemy import text

from database.db_service import DatabaseService
from models.Address import Address
from nodes.node_base import RabbitMQWorkerCallbackBase
from nodes.node_response import NodeResponse
from sql.address import AddressSql


class YourCallbackClass2(RabbitMQWorkerCallbackBase):
    def callback(self, ch, method, properties, body):
        session = DatabaseService()
        db_session = session.get_session()

        sql_query = text(AddressSql.GET_ALL)
        result = db_session.execute(sql_query)
        db_resp = result.fetchall()

        response = Address(
            city=db_resp[0].city,
            street=db_resp[0].street,
            zip=db_resp[0].zip,
            state=db_resp[0].state
        )

        resp_dict = response.to_dict()
        json_string = json.dumps(resp_dict, indent=4)

        NodeResponse.send_http_response(response=json_string, pika=pika, properties=properties, ch=ch, method=method)
