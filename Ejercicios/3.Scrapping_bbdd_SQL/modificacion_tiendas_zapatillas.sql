USE `tienda_zapatillas`;

ALTER TABLE Zapatillas
	ADD COLUMN marca VARCHAR (45) NOT NULL,
    ADD COLUMN talla INT NOT NULL;

ALTER TABLE Empleados
    MODIFY COLUMN salario FLOAT;

ALTER TABLE Clientes
    DROP COLUMN pais;
    
ALTER TABLE Facturas
    ADD COLUMN total FLOAT;

INSERT INTO Zapatillas (id_zapatillas, modelo, color, marca, talla)
	VALUES (1, "XQYUN", "Negro", "Nike", 42),
		   (2, "UOPMN", "Rosas", "Nike", 39),
           (3, "OPNYT", "Verdes", "Adidas", 35);

INSERT INTO Empleados (id_empleados, nombre, tienda, salario, fecha_incorporacion)
	VALUES (1, "Laura", "Alcobendas", 25987, "2010-09-03"),
		   (2, "Maria", "Sevilla", null, "2001-04-11"),
           (3, "Ester", "Oviedo", 30165.98 , "2000-11-29");
           
INSERT INTO Clientes (id_clientes, nombre, numero_telefono, email, direccion, ciudad, provincia, codigo_postal)
	VALUES (1, "Monica", 1234567289, "monica@email.com", "Calle Felicidad", "Móstoles", "Madrid", "28176"),
		   (2, "Lorena", 289345678, "lorena@email.com", "Calle Alegria", "Barcelona", "Barcelona", "12346"),
           (3, "Carmen", 298463759, "carmen@email.com" , "Calle del Color", "Vigo", "Pontevedra","23456");

INSERT INTO Facturas (id_facturas, numero_factura, fecha, id_zapatillas, id_empleado, id_cliente, total)
	VALUES (1, "123", "2001-12-11", 1, 2, 1, 54.98),
		   (2, "1234", "2005-05-23", 1, 1, 3, 89.91),
           (3, "12345", "2015-09-18",2 , 3, 3, 76.23);
           
UPDATE Zapatillas
	SET color = "Amarillo"
    WHERE id_zapatillas = 2;
    
UPDATE Empleados
	SET tienda = "A coruña"
    WHERE id_empleados = 1;
    
UPDATE Clientes
	SET numero_telefono = 123456728
    WHERE id_clientes = 1;

UPDATE Facturas
	SET total = 89.91
    WHERE id_facturas = 2;




    
    
