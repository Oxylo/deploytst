import dash
import dash_core_components as dcc
import dash_html_components as html
import socket


app = dash.Dash()
application = app.server

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        This is Dash running on Azure App Service.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    # For localhost
    # app.run_server(host='0.0.0.0',debug=True, port=8080)
    
    # Both for local host and deployment
    host = socket.gethostbyname(socket.gethostname())
    app.run_server(debug=False, host=host, port = 8080)


