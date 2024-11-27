import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

color_fondo='#a6acaf'

df_subida = pd.read_csv('Pagina_web/banda_subida.csv')
df_bajada=pd.read_csv('Pagina_web/banda_bajada.csv')
df_n_sedes_operador= pd.read_csv('Pagina_web/n_sedes_operador.csv')
df_n_sedes_operador_estado=pd.read_csv('Pagina_web/n_sedes_operador_limpio.csv')


df_subida['promedio total']=df_subida['promedio'].mean()
df_bajada['promedio total']=df_bajada['promedio'].mean()

fig_banda_subida = px.line(
    df_subida,
    x='municipio',
    y=['promedio', 'promedio total'], 
    color_discrete_map={
        "promedio": "#f4d03f ",
        "promedio total": "white",
    }
    
)

fig_banda_subida.update_layout(
    paper_bgcolor=color_fondo,  
    plot_bgcolor=color_fondo,   
    font=dict(color="white"),  
    legend=dict(font=dict(color="white")),  
    xaxis=dict(
        gridcolor="#424949",  # Cuadrícula en gris claro
        zerolinecolor="white",  # Línea del cero en azul oscuro
    ),
    yaxis=dict(
        gridcolor="#424949",  # Cuadrícula en gris claro
        zerolinecolor="white",  # Línea del cero en azul oscuro
    )
)


fig_banda_bajada = px.line(
    df_bajada,
    x='municipio',  
    y=['promedio', 'promedio total'], 
    color_discrete_map={
        "promedio": "#f4d03f ",
        "promedio total": "white",
    }
)

fig_banda_bajada.update_layout(
    paper_bgcolor=color_fondo,  
    plot_bgcolor=color_fondo,   
    font=dict(color="white"),  
    legend=dict(font=dict(color="white")),  
    xaxis=dict(
        gridcolor="#424949",  # Cuadrícula en gris claro
        zerolinecolor="white",  # Línea del cero en azul oscuro
    ),
    yaxis=dict(
        gridcolor="#424949",  # Cuadrícula en gris claro
        zerolinecolor="white",  # Línea del cero en azul oscuro
    )
)

fig_n_sedes_operador= px.bar(
    df_n_sedes_operador,
    x="operador", 
    y="numero de sedes",  
    color="operador",  
    
    barmode="stack", 
)

fig_n_sedes_operador.update_layout(
    paper_bgcolor=color_fondo,  
    plot_bgcolor=color_fondo,   
    font=dict(color="white"),  
    legend=dict(font=dict(color="white")),  
)

fig = px.sunburst(
    df_n_sedes_operador_estado,
    path=["sede","operador", "estado"],  
    values="count",  
    color="count",  
    color_continuous_scale="Viridis",  
    
)
fig.update_layout(
    paper_bgcolor=color_fondo,  
    plot_bgcolor=color_fondo,   
    font=dict(color="white"),  
    legend=dict(font=dict(color="white")),  
)

analisis_subida=dcc.Markdown('''

    **Ventajas:**
    - Facilidad para detectar patrones y áreas con baja capacidad.
    - Visualiza claramente cómo varía el ancho de banda en los municipios.

    **Desventajas:**
    - Puede volverse saturado y difícil de leer con mucha información.'''
    )

analisis_bajada=dcc.Markdown(
    '''
    **Ventajas:**
    - Claridad para observar la tendencia del ancho de banda de bajada.
    - Permite detectar áreas con potenciales problemas de conectividad.
    - Facilita la comparación entre diferentes municipios.

    **Desventajas:**
    - No es adecuado para comparar demasiados municipios.
    - Los valores exactos no son fácilmente legibles sin interacción adicional.
    '''
    )

analisis_sedes= dcc.Markdown(
    '''
    **Ventajas:**
    - Permite una comparación clara entre operadores.
    - Fácil de leer y entender de manera visual.
    - Proporciona una visión rápida de la distribución de sedes por operador.

    **Desventajas:**
    - Se vuelve menos efectivo si se tiene un número muy alto de operadores.
    - Puede resultar menos útil si hay muchos operadores en la misma categoría.
    '''
    )

analisis_sedes_operador_estado= dcc.Markdown(
    '''
    **Ventajas:**
    - Excelente para representar jerárquicamente la distribución de sedes.
    - Facilita la interacción y exploración de datos a diferentes niveles.
    - Visualiza la estructura de datos de manera intuitiva.

    **Desventajas:**
    - Puede ser difícil de leer si hay demasiados niveles de información.
    - Puede resultar confuso para algunos usuarios no familiarizados con este tipo de visualización.
    - Puede volverse saturado y difícil de leer con mucha información.
    '''
    )


app = dash.Dash(__name__)



app.layout = html.Div([
    html.H1("Instituciones esducativas con conexion a internet"),
    html.H2('Promedio ancho de banda de subida por cada municipio'),
    dcc.Graph(id="line-chart1",figure=fig_banda_subida),
    analisis_subida,
    html.H2('Promedio ancho de banda de bajada por cada municipio'),
    dcc.Graph(id="line-chart",figure=fig_banda_bajada),
    analisis_bajada ,
    html.H2('Número de sedes por cada operador'),
    dcc.Graph(id="sunburst-chart",figure=fig_n_sedes_operador),
    analisis_sedes,
    html.H2('Número de sedes agrupadas por operador y estado'),
    dcc.Graph(id="bar-chart",figure=fig),
    analisis_sedes_operador_estado
])


app.run_server(debug=True)
