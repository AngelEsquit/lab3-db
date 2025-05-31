from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import GeneroEnum
from .crud import crear_autor, crear_libro, asignar_autor_a_libro, obtener_autores, obtener_libros
import os
from fastapi import FastAPI
from .models import Libro, Autor

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

def menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Crear autor")
    print("2. Crear libro")
    print("3. Ver todos los autores")
    print("4. Ver todos los libros")
    print("5. Asignar autor a libro")
    print("6. Salir")

def main():
    session = SessionLocal()
    while True:
        menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del autor: ")
            correo = input("Correo del autor: ")
            try:
                autor = crear_autor(session, nombre, correo)
                print(f"Autor creado: {autor.nombre} (ID: {autor.id})")
            except Exception as e:
                print("Error:", e)

        elif opcion == "2":
            titulo = input("Título del libro: ")
            isbn = input("ISBN de 13 dígitos: ")
            if len(isbn) != 13:
                print("El ISBN debe tener 13 dígitos.")
                continue
            print("Géneros disponibles:", [g.value for g in GeneroEnum])
            genero_str = input("Género: ")
            anio = int(input("Año de publicación: "))
            if anio <= 1500:
                print("El año debe ser mayor a 1500.")
                continue    
            try:
                genero = GeneroEnum(genero_str)
                libro = crear_libro(session, titulo, isbn, genero, anio)
                print(f"Libro creado: {libro.titulo} (ID: {libro.id})")
            except ValueError:
                print(f"Error: '{genero_str}' no es un género válido.")
                print("Opciones válidas:", [g.value for g in GeneroEnum])
                session.rollback()
                continue

        elif opcion == "3":
            autores = obtener_autores(session)
            print("\n--- AUTORES ---")
            for a in autores:
                print(f"[{a.id}] {a.nombre} - {a.correo}")

        elif opcion == "4":
            libros = obtener_libros(session)
            print("\n--- LIBROS ---")
            for l in libros:
                print(f"[{l.id}] {l.titulo} ({l.genero.value}) - {l.anio_publicacion} - ISBN: {l.isbn}")
                for autor in l.autores:
                    print(f"   - Autor: {autor.nombre}")

        elif opcion == "5":
            libro_id = int(input("ID del libro: "))
            autor_id = int(input("ID del autor: "))
            try:
                asignar_autor_a_libro(session, libro_id, autor_id)
                print("Autor asignado al libro correctamente.")
            except ValueError:
                print("Error: ID de libro o autor no válido.")
                session.rollback()

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

main()