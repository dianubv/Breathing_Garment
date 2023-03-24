from fastapi import FastAPI
# import database.py

app = FastAPI()


@app.get("/")
def rowot():
    return "hello world"

""" @app.get("/{name}")  
async def root(name:str):
    name=find_item(name)
    return name """



""" def find_item(id):  #sert dans post et delete 
    a = list()
    del a['_id']
    return a """

""" def find_item(id):  #sert dans post et delete 
    for item in TODOLIST:
        if item.id == id:
            return item
    return None """