#
# Goal: plot a scatter plot with the iris dataset
#
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas

df = pandas.read_csv('data/iris.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Draw a scatter plot for data from the setosa species

app.layout = html.Div(children=[
	html.H1(children='Iris'),
	html.Div(children='A demo of Dash (Plotly)'),
    html.Div([
        dcc.Dropdown(
            id='species',
            options=[{'label': i, 'value': i} for i in df.Species.unique() ],
            value='Species'
        ),
    	],
    ),
	dcc.Graph(id='iris-graph')
])

if __name__ == '__main__':
	app.run_server(debug=True)
