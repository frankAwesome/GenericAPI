from flask import Flask, jsonify
from flask_restful import Api
import json
from database.db_service import DatabaseService
from endpoints.hello_world import HelloWorld
from swagger.swagger_setup import SwaggerSetup


app = Flask(__name__)
api = Api(app)

DatabaseService.configure(app=app)

api.add_resource(HelloWorld, '/hello')

# swagger setup
app.register_blueprint(SwaggerSetup.init_swagger(), url_prefix='/swagger')


@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))


if __name__ == '__main__':
    app.run(debug=True)
