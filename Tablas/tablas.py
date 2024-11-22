import pandas as pd
import random
import numpy as np
from datetime import timedelta, datetime

data = pd.read_csv('Datos\INSTITUCIONES_EDUCATIVAS_OFICIALES_DE_MUNICIPIOS_DEL_DEPARTAMENTO_DE_BOYAC__CON_CONEXION_A_INTERNET_20241120.csv')

data_new= data[~data['NOMBRE SEDE EDUCATIVA'].duplicated()]
filas,columnas=data_new.shape

data_i_e=data_new[~data_new['NOMBRE INSTITUCION EDUCATIVA'].duplicated()]

instituciones_educativas=data_i_e[['NOMBRE INSTITUCION EDUCATIVA',
                                   'CODIGO DANE INSTITUCION EDUCATIVA']]


codigo_inte=list(range(2006))
random.shuffle(codigo_inte)
data_new['CODIGO INTERNET']=pd.Series(codigo_inte)
#print(data_new['CODIGO INTERNET'])
data_new['CODIGO INTERNET'].astype(int)

sedes_instituciones_educativas=data_new[['NOMBRE SEDE EDUCATIVA',
                                         'CODIGO DANE SEDE',
                                         'ZONA',
                                         'NOMBRE INSTITUCION EDUCATIVA',
                                         'CODIGO INTERNET']]

data_new['ANCHO DE BANDA DE SUBIDA (MB)']=data_new['ANCHO DE BANDA DE SUBIDA (MB)'].round(1)
data_new['ANCHO DE BANDA DESCARGA (MB)']=data_new['ANCHO DE BANDA DESCARGA (MB)'].round(1)
servicio_internet=data_new[['CODIGO INTERNET',
                            'PROYECTOS DE CONECTIVIDAD 2024',
                            'OPERADOR',
                            'ESTADO',
                            'ANCHO DE BANDA DE SUBIDA (MB)',
                            'ANCHO DE BANDA DESCARGA (MB)']]

inicio = datetime(2017, 1, 30)
final =  datetime(2017, 5, 28)

random_date = [(inicio + (final - inicio) * random.random()).date() for _ in range(filas)]

data_new['FECHAS']=random_date


servir=data_new[['FECHAS',
                 'CODIGO INTERNET',
                 'MUNICIPIO']]


data_mun=data_new[~data_new['MUNICIPIO'].duplicated()]

municipio=data_mun[['MUNICIPIO',
                   'CÓDIGO MUNICIPIO',
                   'DEPARTAMENTO'
                   ]]

data_dep=data_new[~data_new['DEPARTAMENTO'].duplicated()]

departamento= data_dep[['DEPARTAMENTO',
                       'CÓDIGO DEPARTAMENTO']]




instituciones_educativas.to_csv('Tablas/instituciones_educativas.csv', index=False)
sedes_instituciones_educativas.to_csv('Tablas/sedes_instituciones_educativas.csv', index=False)
servicio_internet.to_csv('Tablas/servicio_internet.csv', index=False)
servir.to_csv('Tablas/servir.csv', index=False)
municipio.to_csv('Tablas/municipio.csv', index=False)
departamento.to_csv('Tablas/departamento.csv', index=False)

