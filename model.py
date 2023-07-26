from db import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, TEXT, BOOLEAN, DATE

class Employee(Base):
  __tablename__ = 'employees'

  id = Column( INTEGER( unsigned=True ), primary_key=True, autoincrement=True )
  f_name = Column( TEXT, nullable=False )
  m_name = Column( TEXT )
  l_name = Column( TEXT, nullable=False )
  title = Column( TEXT, nullable=False )
  age = Column( INTEGER( unsigned=True ), nullable=False )
  city = Column( TEXT, nullable=False )
  salary = Column( INTEGER( unsigned=True ) )
  joining = Column( DATE, nullable=False )
  active = Column( BOOLEAN, nullable=False )
