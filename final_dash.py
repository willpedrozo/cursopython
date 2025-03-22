import dash
from dash import dcc, html
import plotly.graph_objs as go

#iniciar nosso aplicativo dash
app = dash.Dash()

#definir nosso layout do dashboard / Div é uma caixinha para organizar melhor os códgiso da linguagem html
app.layout = html.Div([
    html.H1('Gráfico Interativo com Dash e Plotly'),
    dcc.Graph(
        id = 'grafico01',
        figure = {
            'data': [
                go.Scatter(
                    x = [1,2,3,4,5],
                    y = [10,11,12,13,14],
                    mode = 'lines+markers',
                    name = 'Linha 1'
                )
            ],
            'layout' : go.Layout(
                title = 'Gráfico de Linha Interativo',
                xaxis = {'title' : 'Eixo X'},
                yaxis = {'title' : 'Eixo Y'}
            )
        } 
        
    )
]) 

if __name__ == '__main__':
    app.run(debug=True)
