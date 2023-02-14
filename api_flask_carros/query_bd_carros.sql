#CREATE DATABASE bd_carros;

#USE bd_carros;
/*
CREATE TABLE carros(
	id integer not null auto_increment,
    marca varchar(100),
    modelo varchar(100),
    ano integer,
	PRIMARY KEY(id)
);
*/
SELECT * FROM carros;

#SELECT * FROM carros WHERE id = 2;

#INSERT INTO carros(marca, modelo, ano) VALUES ('Renault', 'Clio', 2011);