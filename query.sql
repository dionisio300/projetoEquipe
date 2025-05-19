create database clientes_db;

use clientes_db;

-- id, nome, idade, cidade

create table clientes (
id int primary key auto_increment,
nome varchar(50),
idade int,
cidade varchar(50),
totalCompras decimal(10,2)
);

insert into clientes (nome, idade, cidade, totalCompras) values
('João',35,'Fortaleza',1500.00),
('Maria',25,'Caucaia',2000.00),
('Ana',20,'Fortaleza',5500.00),
('Tiago',22,'caucaia',6000.00),
('Carla',50,'Quixadá',500.00),
('Letícia',20,'Caucaia',7500.00),
('Caio',18,'Fortaleza',1250.00);

select * from clientes;



