import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables del archivo .env

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "una-clave-secreta-por-defecto")  # Clave para firmar JWTs
ALGORITHM = "HS256"  # Algoritmo de encriptación
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Tiempo de expiración del token
