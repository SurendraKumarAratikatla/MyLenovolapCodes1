from sqlalchemy import create_engine
from sqlalchemy import MetaData,Table,column,Integer,String
from sqlalchemy.orm import mapper

db_url = 'mysql+mysqldb://mysql:1134@localhost:3306/mydb'
engine = create_engine(db_url)

metadata = MetaData()

user = Table('user',metadata,
             column('id',Integer,primary_key = True),
             column('name',String(50)),
             column('password',String(50))
             )

class User():
    def __int__(self,name,password):
        self.name = name
        self.password = password

metadata.create_all(engine)
