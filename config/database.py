from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# Configuración de la conexión
DB_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Función para obtener la sesión de la DB (La usamos en los routers)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from apps.auth.models.user import User  # Importar el modelo
Base.metadata.create_all(bind=engine)  # Crear tablas (solo en desarrollo)