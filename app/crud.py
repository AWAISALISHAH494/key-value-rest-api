from sqlalchemy.orm import Session
from . import models, schemas

def create_or_update_key_value(db: Session, key: str, value: str):
    db_item = db.query(models.KeyValue).filter(models.KeyValue.key == key).first()
    
    if db_item:
        db_item.value = value
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        db_item = models.KeyValue(key=key, value=value)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

def get_key_value(db: Session, key: str):
    return db.query(models.KeyValue).filter(models.KeyValue.key == key).first()

def delete_key_value(db: Session, key: str):
    db_item = db.query(models.KeyValue).filter(models.KeyValue.key == key).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False