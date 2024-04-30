from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db
from models.taco import Taco as ModelTaco
from schema import Taco as SchemaTaco
from sqlalchemy import func


taco_router = APIRouter(prefix="/tacos")


@taco_router.get("/")
def get_all_tacos():
    tacos = db.session.query(ModelTaco).all()
    if not tacos:
        raise HTTPException(status_code=404, detail="Sorry, there are no tacos!")
    return tacos


@taco_router.get("/{taco_id}")
def get_taco_by_id(taco_id: int):
    db_taco = db.session.query(ModelTaco).filter(ModelTaco.id == taco_id).first()
    if db_taco is None:
        raise HTTPException(status_code=404, detail="Sorry, couldn't find record of that taco!")
    return db_taco


@taco_router.post("/")
def create_taco(taco: SchemaTaco):
    existing_taco = get_existing_taco(taco.protein, taco.tortilla, taco.has_guac)

    if existing_taco:
        raise HTTPException(status_code=400, detail="Taco not created. This taco already exists!")

    new_taco = ModelTaco(
        protein=taco.protein.capitalize(),
        tortilla=taco.tortilla.capitalize(),
        price=taco.price,
        has_guac=taco.has_guac
    )

    db.session.add(new_taco)
    db.session.commit()
    message = {"message": f"Taco created successfully"}
    return message


@taco_router.put("/{taco_id}")
def update_taco(taco_id: int, taco: SchemaTaco):
    db_taco = db.session.query(ModelTaco).filter(ModelTaco.id == taco_id).first()
    if db_taco is None:
        raise HTTPException(status_code=404, detail="Sorry, couldn't find record of that taco!")

    db_taco.protein = taco.protein
    db_taco.tortilla = taco.tortilla
    db_taco.price = taco.price
    db_taco.has_guac = taco.has_guac

    db.session.commit()
    message = {"message": f"Taco updated successfully"}
    return message


@taco_router.delete("/{taco_id}")
def delete_taco(taco_id: int):
    db_taco = db.session.query(ModelTaco).filter(ModelTaco.id == taco_id).first()
    if db_taco is None:
        raise HTTPException(status_code=404, detail="Sorry, couldn't find record of that taco!")
    
    db.session.delete(db_taco)
    db.session.commit()
    return {"message": f"Taco with ID {taco_id}, has been successfully deleted" }


def get_existing_taco(protein: str, tortilla: str, has_guac: bool):
    protein_lower = protein.lower()
    return db.session.query(ModelTaco).filter(
        func.lower(ModelTaco.protein) == protein_lower,
        ModelTaco.tortilla == tortilla.capitalize(),  # Ensure case-insensitive comparison
        ModelTaco.has_guac == has_guac
    ).first()