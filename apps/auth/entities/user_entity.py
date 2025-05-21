from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    user_handle: str = Field(..., min_length=3, example="ironman")  # Nombre de usuario
    user_password: str = Field(..., min_length=8, example="secret123")  # Contraseña
    user_email: EmailStr = Field(..., example="ironman@mydrugs.com")  # Email válido
    user_name: str = Field(..., min_length=8, example="Tony Stark")  # Nombre real
    user_number: str = Field(..., regex=r'^\+?\d{10,15}$', example="+1234567890")  # Teléfono

class UserResponse(BaseModel):
    user_id: int
    user_handle: str
    user_email: EmailStr

    class Config:
        orm_mode = True