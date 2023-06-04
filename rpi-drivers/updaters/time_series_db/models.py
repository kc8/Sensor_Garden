# Models, which represent tables in the DB
from sqlalchemy import Column, Float, DateTime, Integer
from .engine import engine, Base

class Readings(Base):
    __tablename__ = 'readings'

    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    soil_temperature_1 = Column(Float)
    soil_temperature_2 = Column(Float)
    soil_moisture_1 = Column(Float)
    soil_moisture_2 = Column(Float)
    ambient_temperature = Column(Float)
    ambient_humidity = Column(Float)
    ambient_pressure = Column(Float)

    def __repr__(self):
        return "f{self.date_time}"

Base.metadata.create_all(engine)
