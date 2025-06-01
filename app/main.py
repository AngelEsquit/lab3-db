from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
from .crud import obtener_autores, obtener_libros
import os
from fastapi import FastAPI

DB_URL = os.getenv("DB_URL", "postgresql://postgres:postgres@localhost/lab3")

# Crear conexión y sesión
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)

app = FastAPI()

@app.get("/libros")
def listar_libros():
    session = SessionLocal()
    libros = obtener_libros(session)
    return [
        {
            "id": l.id,
            "titulo": l.titulo,
            "isbn": l.isbn,
            "genero": l.genero.value,
            "anio_publicacion": l.anio_publicacion,
            "autores": [{"id": a.id, "nombre": a.nombre} for a in l.autores]
        }
        for l in libros
    ]

@app.get("/autores")
def listar_autores():
    session = SessionLocal()
    autores = obtener_autores(session)
    return [
        {
            "id": a.id,
            "nombre": a.nombre,
            "correo": a.correo,
            "libros": [{"id": l.id, "titulo": l.titulo} for l in a.libros]
        }
        for a in autores
    ]

@app.get("/indice")
def indice():
    session = SessionLocal()
    result = session.execute(text("SELECT * FROM vista_libros_autores"))
    datos = [
        dict(row)
        for row in result
    ]
    session.close()
    return datos