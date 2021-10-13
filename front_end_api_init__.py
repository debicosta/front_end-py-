import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import Flask, request   

server = Flask(__name__)
app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    html.H1("Simple input example"),
    dcc.Input(
        id='input-x',
        placeholder='Insert x value',
        type='number',
        value='',
    ),
    dcc.Input(
        id='input-y',
        placeholder='Insert y value',
        type='number',
        value='',
    ),
    html.Br(),
    html.Br(),
    html.Div(id='result')
    ])


@app.callback(
    Output('result', 'children'),
    [Input('input-x', 'value'),
     Input('input-y', 'value')]
)

@server.route('/sum', methods=['GET'])
def update_result(x, y):
    result = request.get_json(force = TRUE)
    return "The sum is: {}".format(result)


if __name__ == '__main__':
     app.run_server(host = '0.0.0.0', port = 8050, debug = True, use_reloader=False)
