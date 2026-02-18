from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas, auth
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    hashed = auth.hash_password(user.password)
    db_user = models.User(email=user.email, password=hashed)  # Note: field is 'password', not 'hashed_password'
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Find user by email
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    
    # Check if user exists and password matches
    if not db_user or not auth.verify_password(user.password, db_user.password):  # FIXED: changed from user.hashed_password to db_user.password
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Create token
    token = auth.create_access_token({"sub": db_user.email, "role": db_user.role})
    return {"access_token": token, "token_type": "bearer"}