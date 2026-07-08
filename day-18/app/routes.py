"""
routes.py
---------
API endpoint definitions for the Employee API with authentication.
"""

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserRegister, UserLogin, UserResponse
from app import auth

router = APIRouter()


# Auth Endpoints

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Auth"])
def register(data: UserRegister, db: Session = Depends(get_db)):
    """Register a new user."""
    if auth.get_user_by_username(db, data.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists."
        )
    if auth.get_user_by_email(db, data.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered."
        )
    return auth.register_user(db, data)


@router.post("/login", tags=["Auth"])
def login(data: UserLogin, db: Session = Depends(get_db)):
    """Login with username and password."""
    user = auth.authenticate_user(db, data.username, data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password."
        )
    return {"message": "Login successful", "username": user.username}