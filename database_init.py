from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from data_setup import *

engine =  create_engine('sqlite:///users.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
# categories
user1 = User(name="sakr",
                      id=100,
                      password = "1219")
session.add(user1)
session.commit()



print "Doneee..."