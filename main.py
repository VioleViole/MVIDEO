import pprint
from get_data import parse
from pydantic import BaseModel
from datetime import datetime
from typing import Union
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy import update

DATABASE_URL = "postgresql://postgres:21127097@localhost/postgres"
engine = create_engine(DATABASE_URL)
session = Session(bind=engine)
Base = declarative_base()

class product(Base): #таблица продуктов
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, unique=False, index=True)
    price = Column(Integer, unique=False, index=True)
    description = Column(String, unique=False, index=True)
    rating = Column(Float, unique=False, index=True)
    date = Column(String, unique=False, index=True)

class urls(Base): #таблица с ссылками
    __tablename__ = 'urls'
    url = Column(String, primary_key=True, unique=True, index=True)

def get_product():
    products = {}
    get_products = session.query(product).all()
    for prod in get_products:
        products[prod.id] = [prod.date,prod.name,prod.price,prod.rating,prod.description]

    return products

def take_urls(): #получение всех ссылок из бд
    urls_from_db = session.query(urls.url).all()
    urls_list = [url for url in urls_from_db for url in url]
    return urls_list

def add_urls(url): #добавление ссылки в бд
    url = urls(url=f'https://www.mvideo.ru/products/{url}')
    session.add(url)
    session.commit()

def delete_url(url): # удаление товара по сыллке
    s = delete(urls).where(urls.url == url)
    session.execute(s)
    session.commit()

def get_all_data(urls): #выгрузка данных по ссылке в формате словаря
    products = {}
    for url in urls:
        data = parse(url)
        products[data[0]] = [data[1],data[2],data[3],data[4]]
    return products

def add_product(products): #добавление продукта
    date = str(datetime.today()).split('.')[0]
    for pr in products.items():
        products = product(id=pr[0],name=pr[1][0],price=pr[1][1],description=pr[1][2],rating=pr[1][3],date=date)
        session.add(products)
        session.commit()

def update_product(products): #обновление цен, рейтинга и даты, а также добавление нового продукта, можно зациклить ежечасно
    data_products = session.query(product.id).all()
    date = str(datetime.today()).split('.')[0]
    prod = [x for x in data_products for x in x]
    for pr in products.items():
        if pr[0] in prod:
            print(f'обновление {pr[0]}')
            s = update(product).where(
                product.id == pr[0]
            ).values(
                price=pr[1][1],
                rating=pr[1][3],
                date=date,
            )
            session.execute(s)
        elif pr[0] not in prod:
            print(f'добавление {pr[0]}')
            new_product = product(id=pr[0], name=pr[1][0], price=pr[1][1], description=pr[1][2], rating=pr[1][3],
                               date=date)
            session.add(new_product)
    session.commit()