from pydantic import BaseModel, BaseSettings

class Settings(BaseSettings):
    DATABASE: str = "database.db"

class Config:
    env_file = ".env"

class Item(BaseModel):
    name: str
    price: int
    quantity: int

class Transaction(BaseModel):
    item_id: int
    amount_paid: int
