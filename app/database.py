import os
from sqlalchemy import create_engine, text
from .models import Base

DB_URL = os.getenv("DB_URL", "postgresql://postgres:postgres@localhost/lab3")
engine = create_engine(DB_URL, echo=True)

with engine.connect() as conn:
    conn.execute(text("""
        DO $$
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'isbn13') THEN
                CREATE DOMAIN isbn13 AS VARCHAR(13)
                CHECK (VALUE ~ '^[0-9]{13}$');
            END IF;

            IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'email') THEN
                CREATE DOMAIN email AS VARCHAR(255)
                CHECK (VALUE ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');
            END IF;
        END$$;
    """))

    Base.metadata.create_all(bind=conn)

    conn.execute(text("""
        CREATE OR REPLACE VIEW vista_libros_autores AS
        SELECT 
            l.id AS libro_id,
            l.titulo,
            l.isbn,
            l.genero,
            l.anio_publicacion,
            a.id AS autor_id,
            a.nombre AS autor_nombre,
            a.correo
        FROM libros l
        JOIN autores_libros al ON l.id = al.libro_id
        JOIN autores a ON a.id = al.autor_id;
    """))

    conn.commit()