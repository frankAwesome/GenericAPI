FROM python:3.9

WORKDIR /

COPY /run.py run.py
COPY /generate_models.py generate_models.py
COPY /swagger.json swagger.json
COPY /config.json config.json
COPY /CMakeLists.txt CMakeLists.txt

RUN mkdir /swagger
COPY swagger /swagger

RUN mkdir /database
COPY database /database

RUN mkdir /sql
COPY sql /sql

RUN mkdir /takeons
COPY takeons /takeons

RUN mkdir /endpoints
COPY endpoints /endpoints

RUN apt-get update && apt-get install -y cmake
RUN yes | apt install unixodbc-dev
RUN apt-get update

# Set environment variables for SQL Server ODBC Driver installation
ENV ACCEPT_EULA=Y
ENV MSSQL_SA_PASSWORD=password%401234

# Install prerequisites and SQL Server ODBC Driver
RUN apt-get update && apt-get install -y curl && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    apt-get install -y msodbcsql17

RUN pip install --upgrade pip
RUN pip install -U Flask
RUN pip install -U flask-cors
RUN pip install Flask-RESTful
RUN pip install flask-swagger-ui
RUN pip install pyodbc
RUN pip install Flask SQLAlchemy pyodbc flask-sqlalchemy
RUN pip install Flask pika

RUN mkdir build && cd build && cmake .. && cmake --build . --target generate_models

EXPOSE 5000

CMD [ "python", "run.py" ]