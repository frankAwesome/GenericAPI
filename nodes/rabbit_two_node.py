import json
import pika
from sqlalchemy import text
from models.Address import Address
from tunclibs.node_base import RabbitMQWorkerCallbackBase
from tunclibs.node_response import NodeResponse
from sql.address import AddressSql


class YourCallbackClass2(RabbitMQWorkerCallbackBase):
    def callback(self, ch, method, properties, body):
        sql_query = text(AddressSql.GET_ALL)
        result = self.db_session.execute(sql_query)
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
