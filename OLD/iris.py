#
# Goal: plot a scatter plot with the iris dataset
#
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas

df = pandas.read_csv('/Users/vphan/Dropbox/datasets/iris.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Draw a scatter plot for data from the setosa species

app.layout = html.Div(children=[
	html.H1(children='Iris'),
	html.Div(children='A demo of Dash (Plotly)'),
	dcc.Graph(
		id='iris-graph',
		figure={
			'data': [
				go.Scatter(
					x = df[ df.Species == s ].SepalWidth,
					y = df[ df.Species == s].SepalLength,
					mode = 'markers',
					name = s,
				) for s in df.Species.unique()

			],
			'layout': go.Layout(
				title = 'Iris dataset',
				width = 700,
				height = 700,
			),
		}
	)
])

if __name__ == '__main__':
	app.run_server(debug=True)
