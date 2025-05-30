from sqlalchemy import (
    Column, Integer, String, ForeignKey, Table, create_engine, CheckConstraint,
    Enum, UniqueConstraint, Date, DDL, event
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import DDLElement
import enum

Base = declarative_base()

class GeneroEnum(enum.Enum):
    FICCION = "Ficción"
    NO_FICCION = "No Ficción"
    CIENCIA = "Ciencia"
    HISTORIA = "Historia"

autores_libros = Table(
    'autores_libros', Base.metadata,
    Column('libro_id', ForeignKey('libros.id', ondelete="CASCADE"), primary_key=True),
    Column('autor_id', ForeignKey('autores.id', ondelete="CASCADE"), primary_key=True)
)

class Libro(Base):
    __tablename__ = 'libros'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False, unique=True)
    isbn = Column(String(13), nullable=False, unique=True)
    genero = Column(Enum(GeneroEnum), nullable=False)
    anio_publicacion = Column(Integer, CheckConstraint('anio_publicacion > 1500'), nullable=False)

    autores = relationship("Autor", secondary=autores_libros, back_populates="libros")

class Autor(Base):
    __tablename__ = 'autores'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(255), nullable=False, unique=True)

    libros = relationship("Libro", secondary=autores_libros, back_populates="autores")
