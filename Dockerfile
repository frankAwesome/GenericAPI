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


RUN mkdir build && cd build && cmake .. && cmake --build . --target generate_models

RUN pip install --upgrade pip
RUN pip install -U Flask
RUN pip install -U flask-cors
RUN pip install pyodbc
RUN pip install Flask SQLAlchemy pyodbc flask-sqlalchemy

EXPOSE 5000

CMD [ "python", "run.py" ]