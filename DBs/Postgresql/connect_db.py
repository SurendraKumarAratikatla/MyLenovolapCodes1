import psycopg2
from sqlalchemy import create_engine,orm

conn = psycopg2.connect(host="localhost",user= "postgres",password= "1134",database ="music")

try:
    if conn:
        print("Connection was successful {}".format(conn))
except:
    print("Connection refused")


db_url = 'postgresql+mysqldb://mysql:1134@localhost:3306/test'