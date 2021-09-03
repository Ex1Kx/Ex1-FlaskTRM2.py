CREATE DATABASE inventorysystemdb;
USE inventorysystemdb;

CREATE TABLE billInventory (
product_name varchar(255) NOT NULL,
price varchar(255) NULL,
quantity varchar(255) NULL,
product_id int(11) NOT NULL AUTO_INCREMENT,
PRIMARY KEY (product_id,product_name)
);
CREATE TABLE cajero (
name varchar(50) NOT NULL,
base int(11) DEFAULT NULL,
PRIMARY KEY (name)
);
CREATE TABLE facturas (
codigo int(11) NOT NULL,
cantidad int(11) DEFAULT NULL,
pago varchar(50) DEFAULT NULL,
total int(11) DEFAULT NULL,
PRIMARY KEY (codigo)
) 