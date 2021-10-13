import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import request   

app = dash.Dash()

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

def update_result(x, y):
    query = {'x':'x', 'y':'y'}
    location="get_sum",
    response = requests.get("http://"+ e + ":"+ p,  params=query)
    return "The sum is: {}".format(response.json())


if __name__ == '__main__':
     app.run_server(host = '0.0.0.0', port = 8050, debug = True, use_reloader=False)
