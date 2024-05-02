import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from settings.database import database_settings
from app.api.v1.routes import taco

app = FastAPI()

@app.get("/")
async def root():
    return { "message" : "🌮 Are you hungry for some Tacos?! 🌮"}

# Add DBSessionMiddleware to handle database sessions
app.add_middleware(DBSessionMiddleware, db_url=database_settings.SQLALCHEMY_DATABASE_URL)

# Include the routes from taco.py
app.include_router(taco.taco_router)

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
