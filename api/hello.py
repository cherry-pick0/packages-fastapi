from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/post-test")
def post_test():
    return {"post": "test"}


@app.delete("/delete-test")
def delete_test():
    return {"delete": "test"}
