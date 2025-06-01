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
('Elena Poniatowska', 'elena.poniatowska@example.com'),
('Juan Rulfo', 'juan.rulfo@example.com'),
('Octavio Paz', 'octavio.paz@example.com'),
('Claribel Alegría', 'claribel.alegria@example.com'),
('Alfonsina Storni', 'alfonsina.storni@example.com'),
('Ricardo Piglia', 'ricardo.piglia@example.com'),
('Roberto Bolaño', 'roberto.bolano@example.com'),
('Ana María Matute', 'ana.matute@example.com'),
('Homero Aridjis', 'homero.aridjis@example.com'),
('Cristina Peri Rossi', 'cristina.peri@example.com'),
('Sergio Ramírez', 'sergio.ramirez@example.com'),
('Silvina Ocampo', 'silvina.ocampo@example.com'),
('Juan José Saer', 'juan.saer@example.com'),
('Manuel Puig', 'manuel.puig@example.com'),
('Luisa Valenzuela', 'luisa.valenzuela@example.com'),
('Enrique Vila-Matas', 'enrique.vila@example.com'),
('Pedro Lemebel', 'pedro.lemebel@example.com'),
('Samanta Schweblin', 'samanta.schweblin@example.com'),
('Valeria Luiselli', 'valeria.luiselli@example.com'),
('Guadalupe Nettel', 'guadalupe.nettel@example.com'),
('César Aira', 'cesar.aira@example.com');

-- ====================
-- Insertar libros
-- ====================

INSERT INTO libros (titulo, isbn, genero, anio_publicacion) VALUES
('Cien años de soledad', '9788497592208', 'FICCION', 1967),
('La casa de los espíritus', '9789500727165', 'FICCION', 1982),
('Conversación en La Catedral', '9788432217105', 'FICCION', 1969),
('Rayuela', '9788437604115', 'FICCION', 1963),
('Como agua para chocolate', '9780385420174', 'FICCION', 1989),
('La región más transparente', '9789681604991', 'FICCION', 1958),
('Ficciones', '9780307950925', 'FICCION', 1944),
('La loca de la casa', '9788432217471', 'NO_FICCION', 2003),
('Las venas abiertas de América Latina', '9789682314400', 'HISTORIA', 1971),
('La noche de Tlatelolco', '9789682305774', 'HISTORIA', 1971),
('Pedro Páramo', '9789684115169', 'FICCION', 1955),
('El laberinto de la soledad', '9789681604992', 'NO_FICCION', 1950),
('Cenizas de Izalco', '9789684115176', 'FICCION', 1966),
('Mundo de siete pozos', '9789504910012', 'FICCION', 1934),
('Blanco nocturno', '9788433971977', 'FICCION', 2010),
('Los detectives salvajes', '9788433967758', 'FICCION', 1998),
('Olvidado Rey Gudú', '9788408059119', 'FICCION', 1996),
('1492: Vida y tiempos de Juan Cabezón de Castilla', '9789684115183', 'HISTORIA', 1992),
('La nave de los locos', '9788437604116', 'FICCION', 1984),
('Castigo divino', '9788437604122', 'FICCION', 1988),
('La furia', '9789504910029', 'FICCION', 1959),
('Cicatrices', '9789504910036', 'FICCION', 1969),
('El beso de la mujer araña', '9789504910043', 'FICCION', 1976),
('Cola de lagartija', '9789504910050', 'FICCION', 1983),
('Bartleby y compañía', '9788433971983', 'FICCION', 2000),
('Tengo miedo torero', '9788433971990', 'FICCION', 2001),
('Distancia de Rescate', '9788433972003', 'FICCION', 2015),
('Los ingrávidos', '9788433972010', 'FICCION', 2011),
('El huésped', '9788433972027', 'FICCION', 2006),
('Las noches de Flores', '9788433972034', 'FICCION', 2004);

-- ====================
-- Insertar relaciones autores_libros
-- ====================

INSERT INTO autores_libros (autor_id, libro_id) VALUES
(1, 1),   -- García Márquez -> Cien años de soledad
(2, 2),   -- Isabel Allende -> La casa de los espíritus
(3, 3),   -- Vargas Llosa -> Conversación en La Catedral
(4, 4),   -- Cortázar -> Rayuela
(5, 5),   -- Esquivel -> Como agua para chocolate
(6, 6),   -- Fuentes -> La región más transparente
(7, 7),   -- Borges -> Ficciones
(8, 8),   -- Montero -> La loca de la casa
(9, 9),   -- Galeano -> Las venas abiertas de América Latina
(10, 10), -- Poniatowska -> La noche de Tlatelolco
(11, 11), -- Rulfo -> Pedro Páramo
(12, 12), -- Paz -> El laberinto de la soledad
(13, 13), -- Alegría -> Cenizas de Izalco
(14, 14), -- Storni -> Mundo de siete pozos
(15, 15), -- Piglia -> Blanco nocturno
(16, 16), -- Bolaño -> Los detectives salvajes
(17, 17), -- Matute -> Olvidado Rey Gudú
(18, 18), -- Aridjis -> 1492: Vida y tiempos...
(19, 19), -- Peri Rossi -> La nave de los locos
(20, 20), -- Ramírez -> Castigo divino
(21, 21), -- Ocampo -> La furia
(22, 22), -- Saer -> Cicatrices
(23, 23), -- Puig -> El beso de la mujer araña
(24, 24), -- Valenzuela -> Cola de lagartija
(25, 25), -- Vila-Matas -> Bartleby y compañía
(26, 26), -- Lemebel -> Tengo miedo torero
(27, 27), -- Schweblin -> Distancia de Rescate
(28, 28), -- Luiselli -> Los ingrávidos
(29, 29), -- Nettel -> El huésped
(30, 30), -- Aira -> Las noches de Flores
(1, 16),  -- García Márquez también en Los detectives salvajes
(2, 5),   -- Allende también en Como agua para chocolate
(3, 1),   -- Vargas Llosa también en Cien años de soledad
(4, 3),   -- Cortázar también en Conversación en La Catedral
(7, 4);   -- Borges también en Rayuela