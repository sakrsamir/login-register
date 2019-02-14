import sys
''' the sys module provides a number of 
 functions and variables that can be
 used to manipulate different 
 parts of the python run-time enviroment'''

from sqlalchemy import Column, ForeignKey, Integer, String
# this will come handy when we are writing our mapper code

from sqlalchemy.ext.declarative import declarative_base
# we will use in configration and class code

from sqlalchemy.orm import relationship
# to biuld our foregin key relationships

from sqlalchemy import create_engine
# we will use in our configration code at the end of the file


Base = declarative_base()
''' this will help us get set up when we begin to write our class code
will let SQLAlchemy know that our classes are special SQLALchemy
classes that correspond to tables in our database are special 
SQLALchemy classes that correspond to tables in our database'''


########################--------- Represantation of database as classes------################




class User(Base):
	# make name small chars
	__tablename__ = 'users'

	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	password = Column(String(80), nullable = False)

# at the end

engine = create_engine('sqlite:///users.db')
'''we are using SQLite3
the create engine will create a new file that we can use  
similarly to a more robust database'''  

Base.metadata.create_all(engine)
'''that will go into the database and adds the classes 
we will soon create as a new tables in our database''' 
