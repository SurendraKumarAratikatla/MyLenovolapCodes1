from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker # sessionmaker is for to talk with database
from sqlalchemy.ext.declarative import declarative_base # to create table

engine = create_engine('postgresql://postgres:1134@localhost:5432/mydb')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# creating a table with class

# passing base class into Student as inheritance
class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key= True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(20))

#Base.metadata.create_all(engine) # to migrate this table into our database

#creating an instance of a class to insert a record
student1 = Student(name="Surendra",age = 28,grade="Fifth")
#session.add(student1)
#session.commit()

# insert multiple records
student2 = Student(name="Chinna",age = 30,grade="First")
student3 = Student(name="Kumar",age = 22,grade="Second")
student4 = Student(name="Aratikala",age = 43,grade="Last")
student5 = Student(name="Chinnu",age = 22,grade="Third")

session.add_all([student1,student2,student3,student4,student5])
session.commit()


