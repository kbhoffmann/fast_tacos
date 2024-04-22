import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db
from settings.models import Taco as ModelTaco
from schema import Taco as SchemaTaco

import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()

@app.get("/")
async def root():
    return {"🌮 Are you hungry for some Tacos?! 🌮"}

@app.get('/tacos/')
async def taco():
    tacos = db.session.query(ModelTaco).all()
    if not tacos:
        raise HTTPException(status_code=404, detail="Sorry, there are no tacos!")
    return tacos

@app.get('/taco/{taco_id}', response_model=SchemaTaco)
async def get_taco(taco_id: int):
    db_taco = db.session.query(ModelTaco).filter(ModelTaco.id == taco_id).first()
    if db_taco is None:
        raise HTTPException(status_code=404, detail="Sorry, couldn't find record of that taco!")
    return db_taco

@app.post('/taco/', response_model=SchemaTaco)
async def taco(taco: SchemaTaco):
    db_taco = ModelTaco(protein=taco.protein.capitalize(), tortilla=taco.tortilla.capitalize(), price=taco.price, has_guac=taco.has_guac)
    db.session.add(db_taco)
    db.session.commit()
    return db_taco

@app.put('/taco/{taco_id}', response_model=SchemaTaco)
async def update_taco(taco_id: int, taco: SchemaTaco):
    db_taco = db.session.query(ModelTaco).filter(ModelTaco.id == taco_id).first()
    if db_taco is None:
        raise HTTPException(status_code=404, detail="Sorry, couldn't find record of that taco!")
    
    db_taco.protein = taco.protein
    db_taco.tortilla = taco.tortilla
    db_taco.price = taco.price
    db_taco.price = taco.has_guac
    
    db.session.commit()
    return db_taco

@app.delete('/taco/{taco_id}')
async def delete_taco(taco_id: int):
    db_taco = db.session.query(ModelTaco).filter(ModelTaco.id == taco_id).first()
    if db_taco is None:
        raise HTTPException(status_code=404, detail="Sorry, couldn't find record of that taco!")
    
    db.session.delete(db_taco)
    db.session.commit()
    return {"message": "I hope you're happy! You've Successfully Deleted that Poor taco 😢"}

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)