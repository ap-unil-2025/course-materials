---
layout: project
title: "RESTful API with Authentication"
type: "Programming Concepts"
featured: true
summary: "Modern RESTful API development demonstrating FastAPI, JWT authentication, input validation, automated documentation, and security best practices."
technologies:
  - "FastAPI"
  - "Pydantic"
  - "JWT"
  - "SQLAlchemy"
  - "Uvicorn"
  - "pytest"
tags:
  - "API Development"
  - "Authentication"
  - "Web Security"
  - "Documentation"
  - "Input Validation"
status: "Educational Example"
---

## ⚠️ Educational Content Notice
**This is a DEMO/EDUCATIONAL example showing API development concepts. It is NOT related to any course project and contains no project solutions.**

## Overview

This educational example demonstrates modern RESTful API development using FastAPI, showcasing authentication, input validation, automated documentation, and security best practices. Using a library management system as context, we explore professional web API development patterns.

## Learning Objectives

By studying this example, you will learn:
- **RESTful API Design**: HTTP methods, status codes, and resource modeling
- **Authentication & Authorization**: JWT tokens and security middleware
- **Input Validation**: Request/response validation with Pydantic
- **API Documentation**: Automatic OpenAPI/Swagger documentation
- **Error Handling**: Consistent error responses and exception handling
- **Testing**: API testing strategies and test automation

## Project Structure

```
library-api/
├── src/
│   └── library_api/
│       ├── __init__.py
│       ├── main.py              # FastAPI application
│       ├── config.py            # Configuration
│       ├── auth/
│       │   ├── __init__.py
│       │   ├── models.py        # Auth data models
│       │   ├── handlers.py      # Authentication logic
│       │   └── middleware.py    # Auth middleware
│       ├── books/
│       │   ├── __init__.py
│       │   ├── models.py        # Book data models
│       │   ├── routes.py        # Book API endpoints
│       │   └── service.py       # Business logic
│       ├── users/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   ├── routes.py
│       │   └── service.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── database.py      # Database connection
│       │   ├── security.py      # Security utilities
│       │   └── exceptions.py    # Custom exceptions
│       └── utils/
│           ├── __init__.py
│           └── validators.py    # Custom validators
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_books.py
│   └── test_integration.py
└── requirements.txt
```

## Authentication System

### 1. JWT Authentication Implementation

```python
# src/library_api/auth/models.py
from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from datetime import datetime
import re

class UserRegistration(BaseModel):
    """User registration request model."""
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100)
    full_name: str = Field(..., min_length=2, max_length=100)
    
    @validator('password')
    def validate_password_strength(cls, v):
        """Ensure password meets security requirements."""
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError('Password must contain at least one special character')
        return v

class UserLogin(BaseModel):
    """User login request model."""
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    """Authentication token response."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int  # seconds
    refresh_token: Optional[str] = None

class UserProfile(BaseModel):
    """User profile response model."""
    id: int
    email: str
    full_name: str
    is_active: bool
    is_librarian: bool = False
    created_at: datetime
    last_login: Optional[datetime] = None
    
    class Config:
        from_attributes = True  # For SQLAlchemy compatibility

class TokenData(BaseModel):
    """JWT token payload data."""
    user_id: int
    email: str
    is_librarian: bool = False
    exp: datetime
```

### 2. Security Utilities

```python
# src/library_api/core/security.py
import jwt
import bcrypt
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from fastapi import HTTPException, status
from .config import settings

class SecurityManager:
    """Handles password hashing and JWT operations."""
    
    def __init__(self):
        self.secret_key = settings.secret_key
        self.algorithm = "HS256"
        self.access_token_expire_minutes = 30
        self.refresh_token_expire_days = 7
    
    def hash_password(self, password: str) -> str:
        """Hash a password using bcrypt."""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash."""
        return bcrypt.checkpw(
            plain_password.encode('utf-8'), 
            hashed_password.encode('utf-8')
        )
    
    def create_access_token(self, data: Dict[str, Any]) -> str:
        """Create a JWT access token."""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.access_token_expire_minutes)
        to_encode.update({"exp": expire, "type": "access"})
        
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt
    
    def create_refresh_token(self, data: Dict[str, Any]) -> str:
        """Create a JWT refresh token."""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=self.refresh_token_expire_days)
        to_encode.update({"exp": expire, "type": "refresh"})
        
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt
    
    def verify_token(self, token: str, token_type: str = "access") -> Dict[str, Any]:
        """
        Verify and decode a JWT token.
        
        Args:
            token: JWT token string
            token_type: Expected token type (access or refresh)
            
        Returns:
            Decoded token payload
            
        Raises:
            HTTPException: If token is invalid or expired
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            
            # Verify token type
            if payload.get("type") != token_type:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=f"Invalid token type. Expected {token_type}",
                    headers={"WWW-Authenticate": "Bearer"}
                )
            
            # Check expiration
            exp = payload.get("exp")
            if exp and datetime.fromtimestamp(exp) < datetime.utcnow():
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token has expired",
                    headers={"WWW-Authenticate": "Bearer"}
                )
            
            return payload
            
        except jwt.PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"}
            )

# Global security manager instance
security_manager = SecurityManager()
```

### 3. Authentication Dependencies

```python
# src/library_api/auth/handlers.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.security import security_manager
from ..users.models import User
from .models import TokenData, UserProfile

# HTTP Bearer token scheme
bearer_scheme = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
) -> UserProfile:
    """
    Dependency to get the current authenticated user.
    
    Args:
        credentials: Bearer token from request header
        db: Database session
        
    Returns:
        Current user profile
        
    Raises:
        HTTPException: If authentication fails
    """
    token = credentials.credentials
    
    # Verify and decode token
    payload = security_manager.verify_token(token, "access")
    
    # Get user from database
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user"
        )
    
    return UserProfile.from_orm(user)

async def get_current_librarian(
    current_user: UserProfile = Depends(get_current_user)
) -> UserProfile:
    """
    Dependency to ensure current user is a librarian.
    
    Args:
        current_user: Current authenticated user
        
    Returns:
        Current user if they are a librarian
        
    Raises:
        HTTPException: If user is not a librarian
    """
    if not current_user.is_librarian:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions. Librarian access required."
        )
    
    return current_user

# Optional authentication for public endpoints
async def get_current_user_optional(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(
        HTTPBearer(auto_error=False)
    ),
    db: Session = Depends(get_db)
) -> Optional[UserProfile]:
    """
    Optional authentication dependency.
    
    Returns:
        User profile if authenticated, None otherwise
    """
    if not credentials:
        return None
    
    try:
        return await get_current_user(credentials, db)
    except HTTPException:
        return None
```

## API Endpoints and Validation

### 4. Book Management API

```python
# src/library_api/books/models.py
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime
from enum import Enum

class BookStatus(str, Enum):
    """Book availability status."""
    AVAILABLE = "available"
    BORROWED = "borrowed"
    MAINTENANCE = "maintenance"
    LOST = "lost"

class BookCreate(BaseModel):
    """Book creation request model."""
    title: str = Field(..., min_length=1, max_length=200)
    author: str = Field(..., min_length=1, max_length=100)
    isbn: str = Field(..., regex=r'^[\d-]+$')
    publication_year: int = Field(..., ge=1000, le=datetime.now().year + 1)
    genre: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = Field(None, max_length=1000)
    
    @validator('isbn')
    def validate_isbn(cls, v):
        """Validate ISBN format (basic validation)."""
        # Remove hyphens for validation
        isbn_digits = v.replace('-', '')
        
        if len(isbn_digits) == 10:
            # ISBN-10 validation
            if not isbn_digits[:-1].isdigit():
                raise ValueError('Invalid ISBN-10 format')
        elif len(isbn_digits) == 13:
            # ISBN-13 validation
            if not isbn_digits.isdigit():
                raise ValueError('Invalid ISBN-13 format')
        else:
            raise ValueError('ISBN must be 10 or 13 digits')
        
        return v

class BookUpdate(BaseModel):
    """Book update request model."""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    genre: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[BookStatus] = None

class BookResponse(BaseModel):
    """Book response model."""
    id: int
    title: str
    author: str
    isbn: str
    publication_year: int
    genre: str
    description: Optional[str]
    status: BookStatus
    created_at: datetime
    updated_at: datetime
    
    # Borrowing information (if borrowed)
    borrowed_by: Optional[str] = None  # User full name
    borrowed_at: Optional[datetime] = None
    due_date: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class BookSearchParams(BaseModel):
    """Book search parameters."""
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    status: Optional[BookStatus] = None
    available_only: bool = False
    
    # Pagination
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)

class BookSearchResponse(BaseModel):
    """Paginated book search response."""
    books: List[BookResponse]
    total_count: int
    page: int
    page_size: int
    total_pages: int
```

### 5. Book API Routes

```python
# src/library_api/books/routes.py
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ..core.database import get_db
from ..auth.handlers import get_current_user, get_current_librarian, get_current_user_optional
from ..auth.models import UserProfile
from .models import BookCreate, BookUpdate, BookResponse, BookSearchParams, BookSearchResponse
from .service import BookService

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(
    book_data: BookCreate,
    current_user: UserProfile = Depends(get_current_librarian),
    db: Session = Depends(get_db)
):
    """
    Create a new book (Librarian only).
    
    Requires librarian permissions to add books to the library catalog.
    """
    service = BookService(db)
    
    try:
        book = service.create_book(book_data, created_by=current_user.id)
        return BookResponse.from_orm(book)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/search", response_model=BookSearchResponse)
async def search_books(
    title: Optional[str] = Query(None, description="Search by title"),
    author: Optional[str] = Query(None, description="Search by author"),
    genre: Optional[str] = Query(None, description="Search by genre"),
    available_only: bool = Query(False, description="Show only available books"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    current_user: Optional[UserProfile] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """
    Search books with optional filters and pagination.
    
    Public endpoint with optional authentication for enhanced features.
    """
    search_params = BookSearchParams(
        title=title,
        author=author,
        genre=genre,
        available_only=available_only,
        page=page,
        page_size=page_size
    )
    
    service = BookService(db)
    result = service.search_books(search_params, user=current_user)
    
    return BookSearchResponse(
        books=[BookResponse.from_orm(book) for book in result['books']],
        total_count=result['total_count'],
        page=page,
        page_size=page_size,
        total_pages=(result['total_count'] + page_size - 1) // page_size
    )

@router.get("/{book_id}", response_model=BookResponse)
async def get_book(
    book_id: int,
    current_user: Optional[UserProfile] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """
    Get book details by ID.
    
    Public endpoint with optional authentication for enhanced details.
    """
    service = BookService(db)
    book = service.get_book(book_id, user=current_user)
    
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    
    return BookResponse.from_orm(book)

@router.patch("/{book_id}", response_model=BookResponse)
async def update_book(
    book_id: int,
    book_update: BookUpdate,
    current_user: UserProfile = Depends(get_current_librarian),
    db: Session = Depends(get_db)
):
    """
    Update book information (Librarian only).
    
    Allows partial updates to book details.
    """
    service = BookService(db)
    
    try:
        book = service.update_book(book_id, book_update, updated_by=current_user.id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )
        
        return BookResponse.from_orm(book)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/{book_id}/borrow", response_model=BookResponse)
async def borrow_book(
    book_id: int,
    current_user: UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Borrow a book (Authenticated users only).
    
    Books can only be borrowed if they are currently available.
    """
    service = BookService(db)
    
    try:
        book = service.borrow_book(book_id, user_id=current_user.id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )
        
        return BookResponse.from_orm(book)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/{book_id}/return", response_model=BookResponse)
async def return_book(
    book_id: int,
    current_user: UserProfile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Return a borrowed book.
    
    Only the user who borrowed the book or a librarian can return it.
    """
    service = BookService(db)
    
    try:
        book = service.return_book(book_id, user_id=current_user.id, is_librarian=current_user.is_librarian)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found or not borrowed by you"
            )
        
        return BookResponse.from_orm(book)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    book_id: int,
    current_user: UserProfile = Depends(get_current_librarian),
    db: Session = Depends(get_db)
):
    """
    Delete a book from the catalog (Librarian only).
    
    Books can only be deleted if they are not currently borrowed.
    """
    service = BookService(db)
    
    try:
        success = service.delete_book(book_id, deleted_by=current_user.id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
```

## Error Handling and Middleware

### 6. Custom Exception Handling

```python
# src/library_api/core/exceptions.py
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging
from typing import Union

logger = logging.getLogger(__name__)

class LibraryAPIException(Exception):
    """Base exception for Library API."""
    
    def __init__(self, message: str, status_code: int = 500, details: dict = None):
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)

class BookNotAvailableError(LibraryAPIException):
    """Raised when trying to borrow an unavailable book."""
    
    def __init__(self, book_id: int, current_status: str):
        message = f"Book {book_id} is not available for borrowing"
        details = {"book_id": book_id, "current_status": current_status}
        super().__init__(message, status_code=409, details=details)

class DuplicateResourceError(LibraryAPIException):
    """Raised when trying to create a duplicate resource."""
    
    def __init__(self, resource_type: str, identifier: str):
        message = f"{resource_type} with identifier '{identifier}' already exists"
        details = {"resource_type": resource_type, "identifier": identifier}
        super().__init__(message, status_code=409, details=details)

async def library_exception_handler(request: Request, exc: LibraryAPIException):
    """Handle custom library API exceptions."""
    logger.error(f"Library API error: {exc.message}", extra={"details": exc.details})
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "message": exc.message,
                "type": exc.__class__.__name__,
                "details": exc.details
            }
        }
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle Pydantic validation errors."""
    logger.warning(f"Validation error: {exc.errors()}")
    
    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "message": "Validation failed",
                "type": "ValidationError",
                "details": {
                    "validation_errors": exc.errors()
                }
            }
        }
    )

async def http_exception_handler(request: Request, exc: Union[HTTPException, StarletteHTTPException]):
    """Handle HTTP exceptions."""
    logger.warning(f"HTTP error {exc.status_code}: {exc.detail}")
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "message": exc.detail,
                "type": "HTTPError",
                "status_code": exc.status_code
            }
        }
    )

async def general_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions."""
    logger.error(f"Unexpected error: {str(exc)}", exc_info=True)
    
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "message": "An unexpected error occurred",
                "type": "InternalServerError"
            }
        }
    )
```

## Testing Strategy

### 7. API Testing with pytest

```python
# tests/test_books.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from src.library_api.main import app
from src.library_api.core.database import get_db
from .conftest import override_get_db, create_test_user, create_test_librarian

client = TestClient(app)

class TestBookAPI:
    """Test suite for book management API."""
    
    def test_create_book_as_librarian(self, db_session: Session, librarian_token: str):
        """Test book creation by librarian."""
        book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "isbn": "978-0123456789",
            "publication_year": 2023,
            "genre": "Fiction",
            "description": "A test book"
        }
        
        response = client.post(
            "/books/",
            json=book_data,
            headers={"Authorization": f"Bearer {librarian_token}"}
        )
        
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == book_data["title"]
        assert data["author"] == book_data["author"]
        assert data["status"] == "available"
    
    def test_create_book_as_regular_user_fails(self, db_session: Session, user_token: str):
        """Test that regular users cannot create books."""
        book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "isbn": "978-0123456789",
            "publication_year": 2023,
            "genre": "Fiction"
        }
        
        response = client.post(
            "/books/",
            json=book_data,
            headers={"Authorization": f"Bearer {user_token}"}
        )
        
        assert response.status_code == 403
        assert "Insufficient permissions" in response.json()["error"]["message"]
    
    def test_search_books_public(self, db_session: Session):
        """Test public book search."""
        # First create some test books
        self._create_test_books(db_session)
        
        response = client.get("/books/search?title=Python")
        
        assert response.status_code == 200
        data = response.json()
        assert "books" in data
        assert "total_count" in data
        assert data["page"] == 1
    
    def test_search_books_with_filters(self, db_session: Session):
        """Test book search with filters."""
        self._create_test_books(db_session)
        
        response = client.get("/books/search?genre=Programming&available_only=true")
        
        assert response.status_code == 200
        data = response.json()
        
        # Verify all returned books are available and match genre
        for book in data["books"]:
            assert book["status"] == "available"
            assert book["genre"] == "Programming"
    
    def test_borrow_book_success(self, db_session: Session, user_token: str):
        """Test successful book borrowing."""
        # Create a test book
        book_id = self._create_test_book(db_session)
        
        response = client.post(
            f"/books/{book_id}/borrow",
            headers={"Authorization": f"Bearer {user_token}"}
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "borrowed"
        assert data["borrowed_by"] is not None
        assert data["due_date"] is not None
    
    def test_borrow_unavailable_book_fails(self, db_session: Session, user_token: str):
        """Test borrowing an already borrowed book fails."""
        book_id = self._create_test_book(db_session, status="borrowed")
        
        response = client.post(
            f"/books/{book_id}/borrow",
            headers={"Authorization": f"Bearer {user_token}"}
        )
        
        assert response.status_code == 409  # Conflict
        assert "not available" in response.json()["error"]["message"]
    
    def test_return_book_success(self, db_session: Session, user_token: str):
        """Test successful book return."""
        # Create and borrow a book
        book_id = self._create_borrowed_book(db_session, user_token)
        
        response = client.post(
            f"/books/{book_id}/return",
            headers={"Authorization": f"Bearer {user_token}"}
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "available"
        assert data["borrowed_by"] is None
    
    def test_input_validation(self, db_session: Session, librarian_token: str):
        """Test input validation for book creation."""
        invalid_book_data = {
            "title": "",  # Too short
            "author": "Test Author",
            "isbn": "invalid-isbn",  # Invalid format
            "publication_year": 2030,  # Future year
            "genre": "Fiction"
        }
        
        response = client.post(
            "/books/",
            json=invalid_book_data,
            headers={"Authorization": f"Bearer {librarian_token}"}
        )
        
        assert response.status_code == 422
        error_data = response.json()
        assert "validation_errors" in error_data["error"]["details"]
    
    def test_pagination(self, db_session: Session):
        """Test pagination in book search."""
        # Create multiple test books
        for i in range(25):
            self._create_test_book(db_session, title=f"Book {i}")
        
        # Test first page
        response = client.get("/books/search?page=1&page_size=10")
        assert response.status_code == 200
        data = response.json()
        assert len(data["books"]) == 10
        assert data["page"] == 1
        assert data["total_pages"] >= 3
        
        # Test second page
        response = client.get("/books/search?page=2&page_size=10")
        assert response.status_code == 200
        data = response.json()
        assert len(data["books"]) == 10
        assert data["page"] == 2
    
    def _create_test_books(self, db_session: Session):
        """Helper to create test books."""
        books = [
            {"title": "Python Programming", "genre": "Programming"},
            {"title": "Web Development", "genre": "Programming"},
            {"title": "Fiction Novel", "genre": "Fiction"}
        ]
        
        for book_data in books:
            self._create_test_book(db_session, **book_data)
    
    def _create_test_book(self, db_session: Session, **kwargs):
        """Helper to create a single test book."""
        # Implementation would use your Book model
        # This is a simplified version
        pass
    
    def _create_borrowed_book(self, db_session: Session, user_token: str):
        """Helper to create a borrowed book."""
        book_id = self._create_test_book(db_session)
        # Borrow the book
        client.post(
            f"/books/{book_id}/borrow",
            headers={"Authorization": f"Bearer {user_token}"}
        )
        return book_id
```

## Key API Design Principles

### Best Practices Demonstrated

1. **RESTful Design**: Proper HTTP methods and status codes
2. **Input Validation**: Comprehensive request validation with Pydantic
3. **Authentication**: JWT-based authentication with role-based access
4. **Error Handling**: Consistent error responses and proper exception handling
5. **Documentation**: Automatic OpenAPI/Swagger documentation
6. **Security**: Password hashing, token expiration, input sanitization
7. **Testing**: Comprehensive API testing with different scenarios

### Security Features

- ✅ **Password Security**: Bcrypt hashing with complexity requirements
- ✅ **JWT Authentication**: Secure token-based authentication
- ✅ **Role-Based Access**: Different permissions for users and librarians
- ✅ **Input Validation**: Prevent injection attacks and invalid data
- ✅ **Token Expiration**: Automatic token expiry for security
- ✅ **Error Information**: Limited error information to prevent data leakage

### API Documentation

FastAPI automatically generates interactive documentation:
- **Swagger UI**: Available at `/docs`
- **ReDoc**: Available at `/redoc`
- **OpenAPI Schema**: Available at `/openapi.json`

This example demonstrates professional API development practices essential for building secure, scalable web services.

---

*This example showcases modern web API development with industry-standard security and testing practices.*