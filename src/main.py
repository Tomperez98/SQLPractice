import logging

import sqlalchemy

DATABASE_URL: str = "postgresql+psycopg2://postgres:passw0rd@localhost:5432"
engine = sqlalchemy.create_engine(DATABASE_URL)

with open("sql_queries/Chinook_PostgreSql_utf8.sql", "r") as file:
    sql_alchemy_text = file.read()

with engine.begin() as conn:
    res = conn.execute(sqlalchemy.text(sql_alchemy_text))

logging.info(msg="Database for tutorial is up!")
