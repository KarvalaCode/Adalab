CREATE SCHEMA tienda_zapatillas;

USE tienda_zapatillas;

CREATE TABLE Zapatillas (
id_zapatillas INT AUTO_INCREMENT PRIMARY KEY,
modelo VARCHAR(45) NOT NULL,
color VARCHAR(45) NOT NULL
);

CREATE TABLE Clientes ( 
id_clientes INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(45) NOT NULL,
numero_telefono INT NOT NULL,
email VARCHAR(45) NOT NULL,
direccion VARCHAR(45) NOT NULL,
ciudad VARCHAR(45) NOT NULL,
provincia VARCHAR(45) NOT NULL,
pais VARCHAR(45) NOT NULL,
codigo_postal VARCHAR(45) NOT NULL
);

CREATE TABLE Empleados (
id_empleados INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(45) NOT NULL,
tienda VARCHAR(45) NOT NULL,
salario INT,
fecha_incorporacion DATE not null
);

CREATE TABLE Facturas (
id_facturas INT AUTO_INCREMENT PRIMARY KEY,
numero_factura VARCHAR(45) NOT NULL,
fecha DATE not null,
id_zapatillas INT,
id_empleado INT,
id_cliente INT,
CONSTRAINT fk_facturas_zapatillas
	FOREIGN KEY (id_zapatillas)
    REFERENCES Zapatillas (id_zapatillas)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
CONSTRAINT fk_facturas_empleados
    FOREIGN KEY (id_empleado)
    REFERENCES Empleados (id_empleados)
    ON DELETE SET NULL
	ON UPDATE CASCADE,
CONSTRAINT fk_facturas_clientes
    FOREIGN KEY (id_cliente)
    REFERENCES Clientes (id_clientes)
	ON DELETE SET NULL
    ON UPDATE CASCADE
);
