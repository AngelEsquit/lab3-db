-- ====================
-- Insertar autores
-- ====================

INSERT INTO autores (nombre, correo) VALUES
('Gabriel García Márquez', 'gabriel.garcia@example.com'),
('Isabel Allende', 'isabel.allende@example.com'),
('Mario Vargas Llosa', 'mario.llosa@example.com'),
('Julio Cortázar', 'julio.cortazar@example.com'),
('Laura Esquivel', 'laura.esquivel@example.com'),
('Carlos Fuentes', 'carlos.fuentes@example.com'),
('Jorge Luis Borges', 'jorge.borges@example.com'),
('Rosa Montero', 'rosa.montero@example.com'),
('Eduardo Galeano', 'eduardo.galeano@example.com'),
('Elena Poniatowska', 'elena.poniatowska@example.com');

-- ====================
-- Insertar libros
-- ====================

INSERT INTO libros (titulo, isbn, genero, anio_publicacion) VALUES
('Cien años de soledad', '9788497592208', 'Ficción', 1967),
('La casa de los espíritus', '9789500727165', 'Ficción', 1982),
('Conversación en La Catedral', '9788432217105', 'Ficción', 1969),
('Rayuela', '9788437604115', 'Ficción', 1963),
('Como agua para chocolate', '9780385420174', 'Ficción', 1989),
('La región más transparente', '9789681604991', 'Ficción', 1958),
('Ficciones', '9780307950925', 'Ficción', 1944),
('La loca de la casa', '9788432217471', 'No Ficción', 2003),
('Las venas abiertas de América Latina', '9789682314400', 'Historia', 1971),
('La noche de Tlatelolco', '9789682305774', 'Historia', 1971);

-- ====================
-- Insertar relaciones autores_libros
-- ====================

INSERT INTO autores_libros (autor_id, libro_id) VALUES
(1, 1),  -- García Márquez -> Cien años de soledad
(2, 2),  -- Isabel Allende -> La casa de los espíritus
(3, 3),  -- Vargas Llosa -> Conversación en La Catedral
(4, 4),  -- Cortázar -> Rayuela
(5, 5),  -- Esquivel -> Como agua para chocolate
(6, 6),  -- Fuentes -> La región más transparente
(7, 7),  -- Borges -> Ficciones
(8, 8),  -- Montero -> La loca de la casa
(9, 9),  -- Galeano -> Las venas abiertas de América Latina
(10, 10),-- Poniatowska -> La noche de Tlatelolco

-- Relaciones múltiples
(2, 5),  -- Allende también en Como agua para chocolate
(3, 1),  -- Vargas Llosa también en Cien años
(7, 4),  -- Borges también en Rayuela
(4, 3);  -- Cortázar también en Conversación en La Catedral