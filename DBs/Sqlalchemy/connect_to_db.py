from sqlalchemy import create_engine, orm

db_url = 'mysql+mysqldb://mysql:1134@localhost:3306/test'

engine = create_engine(db_url)

conn = engine.connect()

try:
    print('your connection is okay \n your connection object is: {}',format(conn))

except:
    print('your connection was not connected')