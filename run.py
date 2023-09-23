from flask import Flask, jsonify
from flask_restful import Api
import json
from database.db_service import DatabaseService
from endpoints.hello_world import HelloWorld
from endpoints.rabbit import Rabbit
from endpoints.rabbit_two import RabbitTwo
from swagger.swagger_setup import SwaggerSetup


app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/hello')
api.add_resource(Rabbit, '/rab')
api.add_resource(RabbitTwo, '/rabtwo')

# swagger setup
app.register_blueprint(SwaggerSetup.init_swagger(), url_prefix='/swagger')


@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000)
