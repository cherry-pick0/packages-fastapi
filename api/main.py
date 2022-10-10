import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

import os
from dotenv import load_dotenv
from api import packages, recipients

load_dotenv('../.env')

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


app.include_router(packages.router)
app.include_router(recipients.router)


@app.get("/")
async def root():
    return {"message": "hello world"}


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
