
create table instituciones_educativas(
    nombre varchar(60) primary key,
    codigo_dane varchar(18)
);

create table servicio_internet(
    codigo integer primary key,
    proyecto_de_conectividad varchar(30),
    operador varchar(60),
    estado varchar(35),
    ancho_de_banda_subida numeric(3,1),
    ancho_de_banda_bajada numeric(3,1)
);

create table sedes_instituciones_educativas(
    nombre varchar(80) primary key,
    codigo_dane  varchar(18),
    zona varchar(10) check(zona in ('RURAL','URBANA')),
    nombre_institucion_educativa varchar(60) references instituciones_educativas(nombre),
    codigo_servicio_internet integer references servicio_internet(codigo) 
);

create table departamento(
    nombre varchar(60) primary key,
    codigo varchar(10)
);

create table municipio(
    nombre varchar(40) primary key,
    codigo varchar(10),
    nombre_departamento varchar(60) references departamento(nombre)
);

create table servir(
    fecha date,
    codigo_servicio_internet integer references servicio_internet(codigo),
    nombre_municipio varchar(40) references municipio(nombre)
);

copy instituciones_educativas
from 'C:\Users\Public\Proyecto-ingenieria-de-datos\Tablas\instituciones_educativas.csv'
WITH (FORMAT csv, DELIMITER ',', HEADER true);

copy servicio_internet
from 'C:\Users\Public\Proyecto-ingenieria-de-datos\Tablas\servicio_internet.csv'
WITH (FORMAT csv, DELIMITER ',', HEADER true);

copy sedes_instituciones_educativas
from 'C:\Users\Public\Proyecto-ingenieria-de-datos\Tablas\sedes_instituciones_educativas.csv'
WITH (FORMAT csv, DELIMITER ',', HEADER true);

copy departamento
from 'C:\Users\Public\Proyecto-ingenieria-de-datos\Tablas\departamento.csv'
WITH (FORMAT csv, DELIMITER ',', HEADER true);

copy municipio
from 'C:\Users\Public\Proyecto-ingenieria-de-datos\Tablas\municipio.csv'
WITH (FORMAT csv, DELIMITER ',', HEADER true);

copy servir
from 'C:\Users\Public\Proyecto-ingenieria-de-datos\Tablas\servir.csv'
WITH (FORMAT csv, DELIMITER ',', HEADER true);


select* from departamento
--Eliminar tablas
drop table sedes_instituciones_educativas;
drop table instituciones_educativas;
drop table servir;
drop table servicio_internet;
drop table municipio;
drop table departamento;
