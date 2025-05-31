from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import GeneroEnum
from .crud import crear_autor, crear_libro, asignar_autor_a_libro, obtener_autores, obtener_libros, actualizar_libro, eliminar_libro, actualizar_autor, eliminar_autor
import os

DB_URL = os.getenv("DB_URL", "postgresql://postgres:postgres@localhost/lab3")
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)

def menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Crear autor")
    print("2. Crear libro")
    print("3. Ver todos los autores")
    print("4. Ver todos los libros")
    print("5. Asignar autor a libro")
    print("6. Actualizar libro")
    print("7. Eliminar libro")
    print("8. Actualizar autor")
    print("9. Eliminar autor")
    print("0. Salir")

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
            print("Géneros disponibles:", [g.value for g in GeneroEnum])
            genero_str = input("Género: ")
            anio = int(input("Año de publicación: "))
            try:
                genero = GeneroEnum(genero_str)
                libro = crear_libro(session, titulo, isbn, genero, anio)
                print(f"Libro creado: {libro.titulo} (ID: {libro.id})")
            except Exception as e:
                print("Error:", e)
                session.rollback()

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
            except Exception as e:
                print("Error:", e)
                session.rollback()

        elif opcion == "6":
            libro_id = int(input("ID del libro a actualizar: "))
            titulo = input("Nuevo título (deja vacío para no cambiar): ")
            isbn = input("Nuevo ISBN (deja vacío para no cambiar): ")
            genero_str = input("Nuevo género (deja vacío para no cambiar): ")
            anio = input("Nuevo año de publicación (deja vacío para no cambiar): ")
            try:
                genero = GeneroEnum(genero_str) if genero_str else None
                libro = actualizar_libro(
                    session, libro_id,
                    titulo=titulo or None,
                    isbn=isbn or None,
                    genero=genero,
                    anio=int(anio) if anio else None
                )
                print(f"Libro actualizado: {libro.titulo} (ID: {libro.id})")
            except Exception as e:
                print("Error:", e)
                session.rollback()

        elif opcion == "7":
            libro_id = int(input("ID del libro a eliminar: "))
            try:
                eliminar_libro(session, libro_id)
                print("Libro eliminado correctamente.")
            except Exception as e:
                print("Error:", e)
                session.rollback()

        elif opcion == "8":
            autor_id = int(input("ID del autor a actualizar: "))
            nombre = input("Nuevo nombre (deja vacío para no cambiar): ")
            correo = input("Nuevo correo (deja vacío para no cambiar): ")
            try:
                autor = actualizar_autor(
                    session, autor_id,
                    nombre=nombre or None,
                    correo=correo or None
                )
                print(f"Autor actualizado: {autor.nombre} (ID: {autor.id})")
            except Exception as e:
                print("Error:", e)
                session.rollback()

        elif opcion == "9":
            autor_id = int(input("ID del autor a eliminar: "))
            try:
                eliminar_autor(session, autor_id)
                print("Autor eliminado correctamente.")
            except Exception as e:
                print("Error:", e)
                session.rollback()

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

main()