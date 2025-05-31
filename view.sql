CREATE VIEW vista_libros_autores AS
SELECT
    l.id AS libro_id,
    l.titulo,
    l.isbn,
    l.genero,
    l.anio_publicacion,
    a.id AS autor_id,
    a.nombre AS autor_nombre,
    a.correo AS autor_correo
FROM libros l
JOIN autores_libros al ON l.id = al.libro_id
JOIN autores a ON a.id = al.autor_id; 