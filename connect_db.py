from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
# user и password - это логин и пароль
# localhost - это адрес сервера базы данных
# dbname - это название базы данных.
# create_engine - подключение к базе данных
# "postgresql://user:password@localhost/dbname"
DATABASE_URL = "postgresql://postgres:21127097@localhost/postgres"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

class product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, unique=False, index=True)
    price = Column(Integer, unique=False, index=True)
    description = Column(String, unique=False, index=True)
    rating = Column(Float, unique=False, index=True)
    date = Column(String, unique=False, index=True)

class urls(Base):
    __tablename__ = 'urls'
    url = Column(String, primary_key=True, unique=True, index=True)

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# expose: - 5432:5432