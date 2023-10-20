# How to Execute
1. POST /items/
To add a new item to the vending machine:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Soda",
    "price": 150,
    "quantity": 10
  }'
```

2. GET /items/
To get all items in the vending machine:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/items/' \
  -H 'accept: application/json'
```

3. PUT /items/{item_id}
To update the details of an existing item in the vending machine:

```
curl -X 'PUT' \
  'http://127.0.0.1:8000/items/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Water",
    "price": 100,
    "quantity": 20
  }'
```

4. DELETE /items/{item_id}
To remove an item from the vending machine:

```
curl -X 'DELETE' \
  'http://127.0.0.1:8000/items/1' \
  -H 'accept: application/json'
```

5. POST /buy/
To buy an item from the vending machine:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/buy/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "item_id": 1,
    "amount_paid": 150
  }'
```

6. GET /transactions/

To get all transactions:

```
curl -X 'GET' \
  'http://127.0.0.1:8000/transactions/' \
  -H 'accept: application/json'
```
# How to run
```bash
docker-compose up --build

#port=8000
cd backend
pipenv install -r requirements.txt
uvicorn main:app --reload


docker build -t jinghao/fastapi .
docker run -it -p 8000:8000 jinghao/fastapi
```


```
fastapi_train
├─ Dockerfile
├─ Pipfile
├─ Pipfile.lock
├─ README.md
├─ database.py
├─ docker-compose.yml
├─ main.py
├─ model.py
├─ requirements.txt
├─ utils.py
└─ vending_machine.db

```