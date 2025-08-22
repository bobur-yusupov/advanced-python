from fastapi import FastAPI, HTTPException, Query, Request, Response
from typing import List

from .models import Item, PaginationResponse

app = FastAPI()

items: List[Item] = [] # in-memory database of items

@app.post("/items/", response_model=Item, status_code=201)
async def create_item(item: Item):
    for existing_item in items:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item with this ID is already exist.")
    
    items.append(item)
    return item

@app.get("/items/", response_model=PaginationResponse)
async def read_items(request: Request,
                     skip: int = Query(0, alias="offset", description="Offset for pagination"),
                     limit: int = Query(10, alias="limit", description="Limit for pagination."),
                     read_query: str = Query("", alias="search", description="Search queries for pagination")):
    
    if read_query:
        search_term = read_query.lower()
        filtered_items = [
            item for item in items
            if search_term in item.name.lower() or 
            (item.description and search_term in item.description.lower())
        ]
    else:
        filtered_items = items

    start = skip
    end = skip + limit
    data = filtered_items[start:end]
    total = len(data)

    next_page = (
        f"{request.base_url}items?offset={skip + limit}&limit={limit}&search={read_query}"
        if end < total else None
    )
    previous_page = (
        f"{request.base_url}items?offset={max(0, skip - limit)}&limit={limit}&search={read_query}"
        if skip > 0 else None
    )

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": data,
        "next": next_page,
        "previous": previous_page,
    }

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
        
    raise HTTPException(status_code=404, detail="Item with this ID does not exist.")

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    for index, existing_item in enumerate(items):
        if existing_item.id == item.id:
            items[index] = item
            return item
        
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{items_id}", status_code=204)
async def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            del items[index]

    raise HTTPException(status_code=404, detail="Item not found.")