from app.models import Base
from sqlalchemy import create_engine, MetaData

# Cambia la URL de la base de datos según tu configuración
engine = create_engine('sqlite:///test.db')

# Crear tablas si no existen
Base.metadata.create_all(engine)

# Exportar el DDL a schema.sql
with open('schema.sql', 'w', encoding='utf-8') as f:
    for table in Base.metadata.sorted_tables:
        ddl = str(table.compile(dialect=engine.dialect))
        f.write(ddl + ';')

print("schema.sql generado correctamente.") 