from app.models import Base, Autor, Libro, GeneroEnum, autores_libros
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Cambia la URL de la base de datos según tu configuración
engine = create_engine('sqlite:///test.db')
Session = sessionmaker(bind=engine)
session = Session()

# Crear tablas si no existen
Base.metadata.create_all(engine)

autores = [
    Autor(nombre=f"Autor {i}", correo=f"autor{i}@mail.com") for i in range(1, 11)
]
session.add_all(autores)
session.commit()

libros = [
    Libro(titulo=f"Libro Ficción {i}", isbn=f"97800000000{i:03}", genero=GeneroEnum.FICCION, anio_publicacion=2000+i) for i in range(1, 6)
] + [
    Libro(titulo=f"Libro Ciencia {i}", isbn=f"97800000001{i:03}", genero=GeneroEnum.CIENCIA, anio_publicacion=2010+i) for i in range(1, 5)
] + [
    Libro(titulo=f"Libro Historia {i}", isbn=f"97800000002{i:03}", genero=GeneroEnum.HISTORIA, anio_publicacion=1990+i) for i in range(1, 5)
] + [
    Libro(titulo=f"Libro No Ficción {i}", isbn=f"97800000003{i:03}", genero=GeneroEnum.NO_FICCION, anio_publicacion=2020+i) for i in range(1, 7)
]
session.add_all(libros)
session.commit()

# Relacionar autores y libros (múltiples autores por libro y viceversa)
for i, libro in enumerate(libros):
    # Cada libro tiene al menos 2 autores
    libro.autores.append(autores[i % len(autores)])
    libro.autores.append(autores[(i+1) % len(autores)])
session.commit()

print("Datos de ejemplo insertados correctamente.") 