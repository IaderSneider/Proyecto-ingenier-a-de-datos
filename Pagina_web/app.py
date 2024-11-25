import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px


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
    title="Ancho de banda subida",
)


fig_banda_bajada = px.line(
    df_bajada,
    x='municipio',  
    y=['promedio', 'promedio total'], 
    title="Ancho de banda bajada",

)

fig_n_sedes_operador= px.bar(
    df_n_sedes_operador,
    x="operador",  # Eje X con los diferentes operadores
    y="numero de sedes",  # Eje Y con la cantidad total de cada grupo
    color="operador",  # Color por el estado
    title="Distribución de Count por Operador y Estado",
    barmode="stack",  # apilar las barras para mostrar la distribución por estado
)

fig = px.sunburst(
    df_n_sedes_operador_estado,
    path=["operador", "estado"],  # Estructura jerárquica
    values="count",  # Tamaño de los sectores
    color="count",  # Color basado en la población
    color_continuous_scale="Viridis",  # Escala de colores
    title="Distribución jerárquica de población por región"
)

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1("Gráfico de Líneas Interactivo", style={"textAlign": "center"}),
    dcc.Graph(id="line-chart",figure=fig_banda_subida),
    dcc.Graph(id="line-chart",figure=fig_banda_bajada),
    dcc.Graph(id="sunburst-chart",figure=fig_n_sedes_operador),
    dcc.Graph(id="bar-chart",figure=fig)
])


if __name__ == "__main__":
    app.run_server(debug=True)
