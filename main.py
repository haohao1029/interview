from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import sqlite3
import datetime
from fastapi.middleware.cors import CORSMiddleware
from utils import vending_machine_transaction
from database import add_item, get_items, update_item, delete_item, get_transactions
app = FastAPI()


class Item(BaseModel):
    name: str
    price: int
    quantity: int

class Transaction(BaseModel):
    item_id: int
    amount_paid: int


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/items/")
def create_item(item: Item):
    add_item(item.name, item.price, item.quantity)
    return {"message": "Item added successfully"}


@app.get("/items/")
def read_items():
    return get_items()


@app.put("/items/{item_id}")
def update_item_details(item_id: int, item: Item):
    update_item(item_id, item.name, item.price, item.quantity)
    return {"message": "Item updated successfully"}


@app.delete("/items/{item_id}")
def remove_item(item_id: int):
    delete_item(item_id)
    return {"message": "Item deleted successfully"}

@app.post("/buy/")
def create_transaction(transaction: Transaction):
    result = vending_machine_transaction(transaction.item_id, transaction.amount_paid)
    return {"message": result}


@app.get("/transactions/")
def read_transactions():
    return get_transactions()


