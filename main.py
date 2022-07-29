from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Tree(BaseModel):
    name: str
    location: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/trees/{tree_id}")
def read_trees(tree_id: int, q: Union[str, None] = None):
    return {"tree_id": tree_id, "q": q}

@app.put("/trees/{tree_id}")
def update_tree(tree_id: int, tree: Tree):
    return {"tree_id":tree_id,"tree_name":tree.name}