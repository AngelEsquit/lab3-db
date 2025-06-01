CREATE DOMAIN isbn13 AS VARCHAR(13)
CHECK (VALUE ~ '^[0-9]{13}$');

CREATE TYPE genero_enum AS ENUM ('Ficción', 'No Ficción', 'Ciencia', 'Historia');

CREATE TABLE libros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL UNIQUE,
    isbn isbn13 NOT NULL UNIQUE,
    genero genero_enum NOT NULL,
    anio_publicacion INT CHECK (anio_publicacion > 1500)
);

CREATE TABLE autores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo email NOT NULL UNIQUE
);

CREATE TABLE autores_libros (
    libro_id INT REFERENCES libro(id) ON DELETE CASCADE,
    autor_id INT REFERENCES autor(id) ON DELETE CASCADE,
    PRIMARY KEY (libro_id, autor_id)
);

CREATE VIEW vista_libros_autores AS
SELECT 
    l.id AS libro_id,
    l.titulo,
    l.isbn,
    l.genero,
    a.id AS autor_id,
    a.nombre AS autor_nombre,
    a.correo
FROM libro l
JOIN autores_libros al ON l.id = al.libro_id
JOIN autor a ON a.id = al.autor_id;
