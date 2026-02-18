from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import auth, events, registrations

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Campus Event System API")

# ✅ CRITICAL FIX - Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite default
        "http://127.0.0.1:5173",  # Vite alternative
        "http://localhost:3000",  # React default
        "http://127.0.0.1:3000",  # React alternative
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include routers
app.include_router(auth.router)
app.include_router(events.router)
app.include_router(registrations.router)

@app.get("/")
def root():
    return {"message": "Welcome to AIMs - Smart Campus Event System API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "AIMs Backend"}