from sqlalchemy import (
    Column, Integer, String, ForeignKey, Table, create_engine, CheckConstraint,
    Enum, UniqueConstraint, Date, DDL, event, text
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import DDLElement
from sqlalchemy.ext.declarative import declared_attr
import enum
import re
import os

DB_URL = os.getenv("DB_URL", "sqlite:///test.db")
engine = create_engine(DB_URL)

Base = declarative_base()

class GeneroEnum(enum.Enum):
    FICCION = "Ficción"
    NO_FICCION = "No Ficción"
    CIENCIA = "Ciencia"
    HISTORIA = "Historia"

class ISBNType(String):
    def __init__(self, length=13, **kwargs):
        super().__init__(length, **kwargs)

    def python_type(self):
        return str

    def process_bind_param(self, value, dialect):
        if value is not None:
            if not re.match(r"^\\d{13}$", value):
                raise ValueError("ISBN debe tener exactamente 13 dígitos numéricos")
        return value

autores_libros = Table(
    'autores_libros', Base.metadata,
    Column('libro_id', ForeignKey('libros.id', ondelete="CASCADE"), primary_key=True),
    Column('autor_id', ForeignKey('autores.id', ondelete="CASCADE"), primary_key=True)
)

class Libro(Base):
    __tablename__ = 'libros'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False, unique=True)
    isbn = Column(ISBNType(13), nullable=False, unique=True)
    genero = Column(Enum(GeneroEnum), nullable=False)
    anio_publicacion = Column(Integer, CheckConstraint('anio_publicacion > 1500'), nullable=False)

    autores = relationship("Autor", secondary=autores_libros, back_populates="libros")

class Autor(Base):
    __tablename__ = 'autores'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(255), nullable=False, unique=True)

    libros = relationship("Libro", secondary=autores_libros, back_populates="autores")
