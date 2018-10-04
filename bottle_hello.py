from bottle import route, run, template
import pandas

@route('/')
def index():
	iris = pandas.read_csv('data/iris.csv')
	return template(' {{iris.head()}}', iris=iris)






run(host='localhost', port=8080)