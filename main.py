from fastapi import FastAPI
import db_req

app = FastAPI()

@app.get("/getaccounts/{user_id}")
async def root(user_id: str):
    return db_req.dbquery(user_id)