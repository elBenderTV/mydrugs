from sqlalchemy.orm import Session
from apps.auth.models.user import User

class UserRepository:
    @staticmethod
    def create_user(db: Session, user_data: dict):
        # Crea un usuario en la base de datos (como un guardia que apunta tu nombre en la lista)
        db_user = User(**user_data)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_user_by_handle(db: Session, handle: str):
        # Busca un usuario por su "handle" (como preguntar "¿Ya existe alguien con este apodo?")
        return db.query(User).filter(User.user_handle == handle).first()