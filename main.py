from fastapi import FastAPI

app = FastAPI()


@app.get("/blogs")
def blogs():
  return {"data": "blogs list"}


@app.get("/blogs/unpublished")
def unpublished():
  # fetch all unpublished blogs
  return {"data": "unpublished blogs"}


@app.get("/blogs/{id}")
def blog(id: int):
  # fetch blog with id = id
  return {"data": id}


@app.get("/blogs/{id}/comments")
def comments(id: int):
  # fetch comments of blog with id = id
  return {"data": f"comments of blog with id {id}"}
