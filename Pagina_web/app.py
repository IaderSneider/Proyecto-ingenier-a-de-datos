import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px


df_subida = pd.read_csv('Pagina_web/banda_subida.csv')
df_bajada=pd.read_csv('Pagina_web/banda_bajada.csv')

# Crear gráfico de líneas con Plotly Express
fig_banda_subida = px.line(
    df_subida,
    x='MUNICIPIO',  # El eje X muestra los nombres
    y='ANCHO DE BANDA DE SUBIDA (MB)',   # El eje Y muestra los valores
    title="Ancho de banda subida",
    labels={"nombre": "Nombre", "valor": "Valor"}
)

fig_banda_bajada = px.line(
    df_bajada,
    x='MUNICIPIO',  # El eje X muestra los nombres
    y='ANCHO DE BANDA DESCARGA (MB)',   # El eje Y muestra los valores
    title="Ancho de banda bajada",
    labels={"nombre": "Nombre", "valor": "Valor"}
)

# Inicializar Dash
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Gráfico de Líneas Interactivo", style={"textAlign": "center"}),
    dcc.Graph(id="line-chart",figure=fig_banda_subida),
    dcc.Graph(id="line-chart",figure=fig_banda_bajada)
])

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)
