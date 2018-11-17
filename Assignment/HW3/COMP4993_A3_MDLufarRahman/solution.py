
# Md Lutfar Rahman
# mrahman9@memphis.edu
# DataScience Assingment - 3

import pandas, seaborn, matplotlib, random
from sklearn import linear_model, metrics


df = pandas.read_csv('500_Person_Gender_Height_Weight_Index.csv')	
model  = linear_model.LinearRegression()


def get_training_score(X,y):
	model.fit(X,y)
	return model.score(X,y)

def train_test_split(X, y, test_size = 0.5):
	X_train = []
	X_test = []
	y_train = []
	y_test = []

	for i in range(X.shape[0]):
		if random.random() <=  test_size:
			X_test.append(X.iloc[i])
			y_test.append(y.iloc[i])
		else:
			X_train.append(X.iloc[i])
			y_train.append(y.iloc[i])
	
	X_train = pandas.DataFrame(X_train, columns = X.columns)
	y_train = pandas.Series(y_train)

	X_test = pandas.DataFrame(X_test, columns = X.columns)
	y_test = pandas.Series(y_test)


	return X_train, X_test, y_train, y_test



def validate(X,y, iterations, test_size):

	scores = [ ]
	for i in range(iterations):
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size)
		model.fit(X_train, y_train)
		scores.append(model.score(X_test, y_test))

	return sum(scores)/iterations


def leave_one_out(X, y, i):
	X_train = []
	X_test = []
	y_train = []
	y_test = []

	#print(i,end='')
	X_test.append(X.iloc[i])
	y_test.append(y.iloc[i])
	X_test = pandas.DataFrame(X_test, columns = X.columns)
	y_test = pandas.Series(y_test)

	for j in range(X.shape[0]):
		if j != i:
			X_train.append(X.iloc[i])
			y_train.append(y.iloc[i])

	X_train = pandas.DataFrame(X_train, columns = X.columns)
	y_train = pandas.Series(y_train)

	return X_train, X_test, y_train, y_test



def leave_one_out_cross_validation(X, y):
	scores = [ ]
	y_preds = []
	y_tests = []
	#print(X.size)
	for i in range(X.shape[0]):
		X_train, X_test, y_train, y_test = leave_one_out(X, y, i)
		model.fit(X_train, y_train)
		
		y_pred = model.predict(X_test)
		
		y_preds.append(y_pred)
		y_tests.append(y_test)

		#print(y_test[0], y_pred[0])

	rr = metrics.r2_score(y_tests, y_preds)
	ms_error = metrics.mean_squared_error(y_tests, y_preds)

	return rr, ms_error



def MaleFemaleSeparation():
	X = df[[ 'Weight']]
	y = df['Height']
	training_score = get_training_score(X,y)

	df_male = df[df.Gender == 'Male']
	X = df_male[[ 'Weight']]
	y = df_male['Height']
	training_score_male = get_training_score(X,y)

	df_female = df[df.Gender == 'Female']
	X = df_female[[ 'Weight']]
	y = df_female['Height']
	training_score_female = get_training_score(X,y)

	return training_score, training_score_male, training_score_female


# X = df[['Weight']]
# y = df['Height']
# print(X.shape[0])
# leave_one_out_cross_validation(X, y)