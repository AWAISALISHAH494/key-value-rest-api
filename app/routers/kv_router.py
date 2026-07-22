from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter(prefix="/store", tags=["Key-Value"])

@router.post("/", response_model=schemas.KeyValueResponse, status_code=status.HTTP_201_CREATED)
def store_key_value(item: schemas.KeyValueCreate, db: Session = Depends(get_db)):
    return crud.create_or_update_key_value(db, item.key, item.value)

@router.get("/{key}", response_model=schemas.KeyValueResponse)
def get_value(key: str, db: Session = Depends(get_db)):
    db_item = crud.get_key_value(db, key)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return db_item

@router.put("/{key}", response_model=schemas.KeyValueResponse)
def update_value(key: str, value: str, db: Session = Depends(get_db)):
    db_item = crud.get_key_value(db, key)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return crud.create_or_update_key_value(db, key, value)

@router.delete("/{key}", status_code=status.HTTP_204_NO_CONTENT)
def delete_value(key: str, db: Session = Depends(get_db)):
    deleted = crud.delete_key_value(db, key)
    if not deleted:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"message": "Key deleted successfully"}