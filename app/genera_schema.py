from sqlalchemy.schema import CreateTable
from app.models import Base
from app.database import engine

def generar_schema():
    with open("/app/schema/schema1.sql", "w", encoding="utf-8") as f:
        f.write("""CREATE DOMAIN isbn13 AS VARCHAR(13)
CHECK (VALUE ~ '^[0-9]{13}$');

CREATE DOMAIN email AS VARCHAR(255);

CREATE TYPE genero_enum AS ENUM ('Ficción', 'No Ficción', 'Ciencia', 'Historia');
""")
        for table in Base.metadata.sorted_tables:
            f.write(str(CreateTable(table).compile(engine)) + ";\n\n")
    print("schema.sql generado correctamente.")