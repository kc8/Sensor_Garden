import json
import os
from sqlalchemy import Column, Integer, Float, DateTime, create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



metadata = MetaData()

class Readings(Base):
    __tablename__ = 'readings'

    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    soil_temperature_1 = Column(Float)
    soil_temperature_2 = Column(Float)
    soil_moisture_1 = Column(Float)
    soil_temperature_2 = Column(Float)
    ambient_temperature = Column(Float)
    ambient_humidity = Column(Float)
    ambient_pressure = Column(Float)

    def __repr__(self):
        return "f{self.date_time}"

DBSession = sessionmaker(bind=engine)
session = DBSession()
Base.metadata.create_all(engine)
