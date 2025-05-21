from config.database import Base, engine
from apps.auth.models.user import User  # Ahora no hay ciclo

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas exitosamente!")

if __name__ == "__main__":
    create_tables()