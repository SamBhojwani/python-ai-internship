"""
auth_routes.py
--------------
Authentication endpoints - register, login, me.
"""

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserRegister, UserLogin, UserResponse
from app.dependencies import get_current_user
from app.models import User
from app.services import auth_service
from app import security
from app.logger import logger

router = APIRouter(tags=["Auth"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    responses={
        201: {"description": "User registered successfully"},
        400: {"description": "Username or email already exists"}
    }
)
def register(data: UserRegister, db: Session = Depends(get_db)):
    """Register a new user with a username, email, password and role. Passwords are hashed before storage."""
    if auth_service.get_user_by_username(db, data.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists.")
    if auth_service.get_user_by_email(db, data.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered.")
    return auth_service.register_user(db, data)


@router.post(
    "/login",
    summary="Login and receive a JWT token",
    responses={
        200: {"description": "Login successful, returns JWT token"},
        401: {"description": "Invalid username or password"}
    }
)
def login(data: UserLogin, db: Session = Depends(get_db)):
    """Login with username and password. Returns a JWT access token valid for 30 minutes."""
    user = auth_service.authenticate_user(db, data.username, data.password)
    if not user:
        logger.warning(f"Failed login attempt for username: {data.username}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password.")
    token = security.create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.get(
    "/me",
    response_model=UserResponse,
    summary="Get current logged in user",
    responses={
        200: {"description": "Returns current user info"},
        401: {"description": "Invalid or expired token"}
    }
)
def get_current_user_info(current_user: User = Depends(get_current_user)):
    """Returns the profile of the currently authenticated user."""
    return current_user