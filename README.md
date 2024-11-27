# Proyecto ingenieria de datos
### Paginas donde se tomaron los datos:  
- [Instituciones educativas de Boyacá con acceso a interner  ](https://www.datos.gov.co/Ciencia-Tecnolog-a-e-Innovaci-n/INSTITUCIONES-EDUCATIVAS-OFICIALES-DE-MUNICIPIOS-D/xrdq-pb8b/about_data)  
[Archivo](Datos/INSTITUCIONES_EDUCATIVAS_OFICIALES_DE_MUNICIPIOS_DEL_DEPARTAMENTO_DE_BOYAC__CON_CONEXION_A_INTERNET_20241120.csv)  

- [Municipios](https://co.wikimedia.org/wiki/Municipios)  
[Archivo](Tablas/municipio.csv)

- [Departamentos](https://www.dian.gov.co/atencionciudadano/formulariosinstructivos/Formularios/2012/departamentos_2012.pdf)   
[Aechivo](Tablas/departamento.csv)

# Apreciaciones del Proceso de Desarrollo del Proyecto

El desarrollo del proyecto de implicó varias etapas. A continuación, presento mis apreciaciones respecto a cada aspecto clave del proceso:

### Selección de Fuentes de Datos
- **Desafíos:**  
  En algunos casos, la consolidación y limpieza de los datos (por ejemplo, manejo de formatos, valores nulos o duplicados) puede haberse convertido en un paso laborioso. 

### Diseño de la Base de Datos
- **Aciertos:**  
  La elección de **PostgreSQL** como sistema gestor de base de datos fue adecuada, dada su capacidad para manejar datos estructurados y consultas complejas. El diseño probablemente permitió una estructura clara, con tablas bien normalizadas para facilitar consultas y evitar redundancias.
- **Desafíos:**  
  Una etapa crítica fue modelar adecuadamente las relaciones entre entidades como municipios, instituciones educativas y operadores. Asegurarse de incluir índices y claves primarias/foráneas bien definidas.


### Carga de Datos

- **Desafíos:**  
  Validar la calidad de los datos durante la carga (como formatos de fechas, latitudes y longitudes) es siempre una tarea que requiere atención especial.

## Conexión con la Base de Datos
- **Aciertos:**  
  Usar bibliotecas como **psycopg2** para conectar PostgreSQL con python facilitó las consultas y la integración de datos.

### Desarrollo Usando Dash
- **Aciertos:**  
  Dash demostró ser una excelente elección para el desarrollo de las visualizaciones interactivas y la interfaz del proyecto.
- **Desafíos:**  
  Diseñar un layout atractivo y funcional en Dash puede ser complejo, especialmente si se desea un diseño altamente personalizado.

# Conclusión
El proyecto destaca por su capacidad para generar percepciones útiles sobre la conectividad en instituciones educativas, con aplicaciones prácticas tanto para la planificación pública como para los operadores de servicios de internet. Las herramientas seleccionadas, combinadas con un enfoque sistemático, demuestran un manejo sólido de tecnologías modernas y metodologías de desarrollo de software. Una mayor automatización y mejoras en el diseño visual serían los próximos pasos ideales para escalar el impacto del proyecto.



