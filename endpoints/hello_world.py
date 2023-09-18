from flask_restful import Resource, current_app
from flask import jsonify
from sqlalchemy.sql import text
from models.Address import Address
from sql.address import AddressSql


class HelloWorld(Resource):
    def get(self):
        sql_query = text(AddressSql.GET_ALL)
        result = current_app.db.session.execute(sql_query)
        db_resp = result.fetchall()

        response = Address(
                city=db_resp[0].city,
                street=db_resp[0].street,
                zip=db_resp[0].zip,
                state=db_resp[0].state
            )

        return jsonify(response.to_dict())
