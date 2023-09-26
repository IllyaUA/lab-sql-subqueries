from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Film(Base):
    __tablename__ = 'film'

    film_id = Column(Integer, primary_key=True)
    title = Column(String)
    # Define other columns...

class Inventory(Base):
    __tablename__ = 'inventory'

    inventory_id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('film.film_id'))
    inventory_status = Column(String)
    # Define other columns...
