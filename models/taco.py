from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Numeric, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import func
from settings.database import database_settings, DatabaseSettings

engine = create_engine(database_settings.SQLALCHEMY_DATABASE_URL)

Base  = declarative_base()

class Taco(Base):
    __tablename__ = 'taco'
    id  = Column(Integer, primary_key=True, index=True)
    protein = Column(String)
    tortilla = Column(String, default='Corn')
    price = Column(Numeric(precision=10, scale=2))
    has_guac = has_guac = Column(Boolean, default=True) 
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)