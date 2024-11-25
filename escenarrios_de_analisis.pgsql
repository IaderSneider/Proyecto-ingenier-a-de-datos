
copy(
    select nombre as municipio,avg(ancho_de_banda_subida) as promedio
    from municipio join servir on municipio.nombre=servir.nombre_municipio
                join servicio_internet on servicio_internet.codigo=servir.codigo_servicio_internet
    where estado = 'EN OPERACIÓN'
    GROUP by nombre)
TO 'C:\Users\Public\Proyecto-ingenieria-de-datos\Pagina_web\banda_subida.csv' DELIMITER ',' CSV HEADER;

copy(
    select nombre as municipio,avg(ancho_de_banda_bajada) as promedio
    from municipio join servir on municipio.nombre=servir.nombre_municipio
                join servicio_internet on servicio_internet.codigo=servir.codigo_servicio_internet
    where estado = 'EN OPERACIÓN'
    GROUP by nombre)
TO 'C:\Users\Public\Proyecto-ingenieria-de-datos\Pagina_web\banda_bajada.csv' DELIMITER ',' CSV HEADER;

copy(
    select operador,count(nombre) as "numero de sedes"
    from sedes_instituciones_educativas join servicio_internet
        on sedes_instituciones_educativas.codigo_servicio_internet=servicio_internet.codigo
    group by operador)
TO 'C:\Users\Public\Proyecto-ingenieria-de-datos\Pagina_web\n_sedes_operador.csv' DELIMITER ',' CSV HEADER;

copy(
    select operador, estado, count(nombre)
        from sedes_instituciones_educativas join servicio_internet
        on sedes_instituciones_educativas.codigo_servicio_internet=servicio_internet.codigo
    group by rollup(operador,estado))
TO 'C:\Users\Public\Proyecto-ingenieria-de-datos\Pagina_web\n_sedes_operador_estado.csv' DELIMITER ',' CSV HEADER;

