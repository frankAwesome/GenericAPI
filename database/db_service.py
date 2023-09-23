import json
from flask_sqlalchemy import SQLAlchemy


class DatabaseService:
    @staticmethod
    def configure(app):
        # Read configuration from config.json
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)

        # Extract SQL Server connection details from the config
        sql_server_config = config.get('sql_server', {})
        server = sql_server_config.get('server', 'localhost')
        database = sql_server_config.get('database', 'YourDatabaseName')
        username = sql_server_config.get('username', 'sa')
        password = sql_server_config.get('password', 'YourPasswordHere')
        driver = sql_server_config.get('driver', 'ODBC Driver 17 for SQL Server')

        # Configure SQLAlchemy with the extracted values
        # app.config[
        #     'SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver};TrustServerCertificate=yes"

        app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://SA:password%401234@localhost:1433/TestProject?driver=ODBC+Driver+17+for+SQL+Server'


        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        app.db = SQLAlchemy(app)
