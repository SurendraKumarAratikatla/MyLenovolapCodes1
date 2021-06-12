import sqlalchemy
from sqlalchemy import create_engine,orm

engine = create_engine('postgresql://postgres:1134@localhost:5432/music')

conn = engine.connect()

try:
    print('your connection is okay \n your connection object is: {}',format(conn))

except:
    print('your connection was not connected')