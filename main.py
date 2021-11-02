from fastapi import FastAPI

app = FastAPI()


@app.get("/blogs")
def blogs(limit = 10, published = False):
  # fetch all blogs
  if published:
    return {"data": f"{limit} published blogs from db"}
  else:
    return {"data": f"{limit} blogs from db"}


@app.get("/blogs/unpublished")
def unpublished():
  # fetch all unpublished blogs
  return {"data": "unpublished blogs"}


@app.get("/blogs/{id}")
def blog(id: int):
  # fetch one blog with id
  return {"data": id}


@app.get("/blogs/{id}/comments")
def comments(id: int):
  # fetch all comments of blog with id = id
  return {"data": f"comments of blog with id {id}"}
