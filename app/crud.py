from sqlalchemy.orm import Session
from .models import Libro, Autor, GeneroEnum

def crear_autor(db: Session, nombre: str, correo: str):
    autor = Autor(nombre=nombre, correo=correo)
    db.add(autor)
    db.commit()
    db.refresh(autor)
    return autor

def crear_libro(db: Session, titulo: str, isbn: str, genero: GeneroEnum, anio: int):
    libro = Libro(titulo=titulo, isbn=isbn, genero=genero, anio_publicacion=anio)
    db.add(libro)
    db.commit()
    db.refresh(libro)
    return libro

def asignar_autor_a_libro(db: Session, libro_id: int, autor_id: int):
    libro = db.query(Libro).get(libro_id)
    autor = db.query(Autor).get(autor_id)
    libro.autores.append(autor)
    db.commit()

def obtener_libros(db: Session):
    return db.query(Libro).all()

def obtener_autores(db: Session):
    return db.query(Autor).all()

def actualizar_libro(db: Session, libro_id: int, titulo: str = None, isbn: str = None, genero: GeneroEnum = None, anio: int = None):
    libro = db.query(Libro).get(libro_id)
    if not libro:
        raise ValueError("Libro no encontrado")
    if titulo is not None:
        libro.titulo = titulo
    if isbn is not None:
        libro.isbn = isbn
    if genero is not None:
        libro.genero = genero
    if anio is not None:
        libro.anio_publicacion = anio
    db.commit()
    db.refresh(libro)
    return libro

def eliminar_libro(db: Session, libro_id: int):
    libro = db.query(Libro).get(libro_id)
    if not libro:
        raise ValueError("Libro no encontrado")
    db.delete(libro)
    db.commit()

def actualizar_autor(db: Session, autor_id: int, nombre: str = None, correo: str = None):
    autor = db.query(Autor).get(autor_id)
    if not autor:
        raise ValueError("Autor no encontrado")
    if nombre is not None:
        autor.nombre = nombre
    if correo is not None:
        autor.correo = correo
    db.commit()
    db.refresh(autor)
    return autor

def eliminar_autor(db: Session, autor_id: int):
    autor = db.query(Autor).get(autor_id)
    if not autor:
        raise ValueError("Autor no encontrado")
    db.delete(autor)
    db.commit()
