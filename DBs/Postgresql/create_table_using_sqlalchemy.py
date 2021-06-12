from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker # sessionmaker is for to talk with database
from sqlalchemy.ext.declarative import declarative_base # to create table

engine = create_engine('postgresql://postgres:1134@localhost:5432/mydb')

Session = sessionmaker(bind=engine)
#session = Session()

Base = declarative_base()

# creating a table with class

# passing base class into Student as inheritance
class Student(Base):
    __tablename__ = "Student1"

    id = Column(Integer, primary_key= True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(20))

Base.metadata.create_all(engine) # to migrate this table into our database


