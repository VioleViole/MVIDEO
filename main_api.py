import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy import update
from sqlalchemy import delete
from main import get_all_data,add_product,update_product,add_urls,take_urls,get_product,delete_url,product,urls

app = FastAPI()

@app.get("/products/{id}") # выдача определенного товара по его id
def get_products(id: int):
    produ = get_product()
    return f'Дата обновления: {produ[id][0]}  ||| ' \
           f'Наименование: {produ[id][1]}  ||| ' \
           f'Цена: {produ[id][2]}  ||| ' \
           f'Рейтинг: {produ[id][3]}  ||| ' \
           f'Описание: {produ[id][4]}'

@app.get("/products") # выдача всей информации
def products_all():
    produ = get_product()
    return produ

@app.get("/add_url/{url}") # https://www.mvideo.ru/products/(добавлять остаток сылки сюда)
def add_url(url: str):
    add_urls(url)
    return f"{url} был добавлен в базу!"

@app.get("/delete_url/{url}") # так же как и с добавлением
def delete_product(url: str):
    delete_url(url)
    return f"{url} Удалён из базы!"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5432)