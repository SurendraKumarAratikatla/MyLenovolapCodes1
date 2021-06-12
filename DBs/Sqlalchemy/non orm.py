from sqlalchemy import create_engine

db_url = 'mysql+mysqldb://mysql:1134@localhost:3306/mydb'
engine = create_engine(db_url)

cursor = engine.connect()
query = 'select * from customers'

result = cursor.execute(query)

for value in result:
    print('name : {}'.format(value[1]))
    print('branch : {}'.format(value[2]))
    print('age : {}'.format(value[3]))
    print('salary : {}'.format(value[4]))
