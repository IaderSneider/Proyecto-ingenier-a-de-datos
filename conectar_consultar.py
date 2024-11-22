from psycopg2 import connect
try:
    conexion=connect(host='localhost',
                    user='postgres',
                    password='123456789',
                    database='proyecto',
                    port='5432')
    print('Conexion exitosa ...')

    cursor= conexion.cursor()
    def imprime(tabla):
        print('---------------------',tabla,'--------------------------------------')
        cursor.execute(f'select * from {tabla}')
        rows=cursor.fetchall()
        flag=0
        cantidad_datos=20
        for row in rows:
            print(row)
            flag +=1
            if flag>=cantidad_datos:
                break
        print('--------------------------------------------------------------')
    imprime('departamento')
    imprime('instituciones_educativas')
    imprime('municipio')
    imprime('sedes_instituciones_educativas')
    imprime('servicio_internet')
    imprime('servir')
except:
    print('Fallo conexion, cambie el puerto')
finally:
    conexion.close()
    print('Conexion finalizada')



