import models.users
import schemas.users
from sqlalchemy.orm import Session

def get_user(db: Session, ID: int):
    return db.query(models.users.User).filter(models.users.User.ID == ID).first()

def get_user_by_usuario(db: Session, usuario: str):
    return db.query(models.users.User).filter(models.users.User.Nombre_Usuario == usuario).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.users.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.users.UserCreate):
    db_user = models.users.User(
        Persona_ID=user.Persona_ID,
        Nombre_Usuario=user.Nombre_Usuario,
        Correo_Electronico=user.Correo_Electronico,
        Password=user.Password,
        Numero_Telefonico_Movil=user.Numero_Telefonico_Movil,
        Estatus=user.Estatus,
        Fecha_Registro=user.Fecha_Registro,
        Fecha_Actualizacion=user.Fecha_Actualizacion
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, ID: int, user: schemas.users.UserUpdate):
    db_user = db.query(models.users.User).filter(models.users.User.ID == ID).first()
    if db_user:
        for var, value in vars(user).items():
            if value is not None:
                setattr(db_user, var, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, ID: int):
    db_user = db.query(models.users.User).filter(models.users.User.ID == ID).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
