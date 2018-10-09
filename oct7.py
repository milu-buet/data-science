import pandas,numpy



def get_data():
	return pandas.read_csv('data/cali_housing.csv')


def process_data(df):

	#drop missing value rows
	df.dropna(inplace=True)

	#descretizing
	df['income_cat'] = numpy.ceil(df.median_income / 1.5)
	df['income_cat'] = df/income_cat.where( df.income_cat < 6, 6)

	#convert ocean proximity to non-categorical
	return pandas.get_dummies(df, columns = ['ocean_proximity'])


df = get_data()
df = process_data(df)

#print(df.columns)

y = df.median_house_value
#X = df