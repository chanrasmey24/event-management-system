from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models
from ..deps import get_current_user

router = APIRouter(prefix="/registrations", tags=["Registrations"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/{event_id}")
def register_event(event_id: int, user=Depends(get_current_user), db: Session = Depends(get_db)):
    obj = models.Registration(user_id=1, event_id=event_id)
    db.add(obj)
    db.commit()
    return {"msg": "Registered"}
