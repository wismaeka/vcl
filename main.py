from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/names/{name}")
def read_name(name):
    return {"name": name, "message": f"Hello, my name is {name}"}


@app.get("/items/{id}")
def read_items(id):
    return {"id": id}
