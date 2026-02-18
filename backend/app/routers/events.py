from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas
from ..deps import get_current_user

router = APIRouter(prefix="/events", tags=["Events"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/", response_model=schemas.EventOut)
def create_event(event: schemas.EventBase, user=Depends(get_current_user), db: Session = Depends(get_db)):
    obj = models.Event(**event.dict(), creator_id=1)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=list[schemas.EventOut])
def list_events(db: Session = Depends(get_db)):
    return db.query(models.Event).all()

@router.post("/", response_model=schemas.RegistrationOut)
def register_event(
    data: schemas.RegistrationCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    existing = db.query(models.Registration).filter(
        models.Registration.user_id == current_user.id,
        models.Registration.event_id == data.event_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Already registered")

    registration = models.Registration(
        user_id=current_user.id,
        event_id=data.event_id
    )

    db.add(registration)
    db.commit()
    db.refresh(registration)

    return registration
