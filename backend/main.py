from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm.session import Session
from database import get_db

from models.property import Property
from settings import cors

app = FastAPI()


app.add_middleware(CORSMiddleware, **cors)


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}


@app.get("/property/{property_id}")
def read_property(property_id: int, db: Session = Depends(get_db)):
    project = db.query(Property).get(property_id)
    project.split_images()
    project_dict = project.__dict__
    project_dict["agent"] = project.agent.__dict__
    return project


@app.get("/properties")
def read_properties(db: Session = Depends(get_db), q: str = "", page: int = 1):
    limit = 9
    offset = (page - 1) * limit
    q = q.lower().strip()
    if q == "":
        properties = db.query(Property).offset(offset).limit(limit).all()
        total_props = db.query(Property).count()
    else:
        properties = (
            db.query(Property)
            .filter(
                Property.title.like(f"%{q}%")
            )
            .offset(offset)
            .limit(limit)
            .all()
        )
        total_props = (
            db.query(Property)
            .filter(
                Property.title.like(f"%{q}%")
            )
            .count()
        )
    for prop in properties:
        prop.split_images()
    return {
        "results": properties,
        "page": page,
        "post_per_page": limit,
        "total": total_props,
    }
