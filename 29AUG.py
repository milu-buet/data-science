

def get_sepal_width(filename, key):
	
	data_file= open(filename)
	header = data_file.readline()
	column = header.split(',').index(key)
	widths = []
	
	for line in data_file:
		#line = line.strip()
		
		item = line.strip().split(',')[column]
		widths.append(float(item))
		#print(item)

	data_file.close()
	return widths


def get_column(filename, key, condition):
	output = []
	data_file = open(filename)
	keys = data_file.readline().split(',')

	if key not in keys:
		raise Exception('Unknown key')

	column = keys.index(key)

	for line in data_file:
		#line = line.strip()
		
		items = line.strip().split(',')
		item = items[column]

		if condition(items):
			output.append(float(item))
		#print(item)

	data_file.close()
	return output



def setosa(items):
	return items[-1] == 'setosa'


sw = get_column('iris.csv','SepalWidth', setosa)
print(sw)


