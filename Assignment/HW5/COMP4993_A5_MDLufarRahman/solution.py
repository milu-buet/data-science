# Md Lutfar Rahman
# mrahman9@memphis.edu
# DataScience Assingment - 5

import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

import pandas
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import precision_score, recall_score


df = pandas.read_csv('iris.csv')
X = df[['SepalLength', 'SepalWidth', 'PetalWidth', 'PetalLength']]
y = df['Species']


def Q1():
	models = [NearestCentroid(), KNeighborsClassifier(), DecisionTreeClassifier()]
	names = ['NearestCentroid', 'KNN', 'DecisionTree']

	precision = [0]*3
	recall = [0]*3

	kf = KFold(n_splits=10)   # 10 fold cross validation
	for train_index, test_index in kf.split(X):
		X_train, X_test = X.ix[train_index], X.ix[test_index]
		y_train, y_test = y.ix[train_index], y.ix[test_index]

		for i,model in enumerate(models):
			model.fit(X_train, y_train)
			y_pred = model.predict(X_test)
			
			precision[i] += precision_score(y_pred, y_test, average='macro')
			recall[i] += recall_score(y_pred, y_test, average='macro')
	
	print('')
	row_format ="{:>20}" * (3)
	print(row_format.format('Classifier', 'Precision', 'Recall'))
	print('')
	for i in range(3):
		print( row_format.format(names[i], round(precision[i]/10.0,2),  round(recall[i]/10.0, 2)))



def Q2():
	
	max_depth = [4,5,6]
	min_samples_leaves = [3,4,5]
	precision = {}
	recall = {}

	kf = KFold(n_splits=10)   # 10 fold cross validation


	for i in range(len(max_depth)):
		for j in range(len(min_samples_leaves)):
			model = DecisionTreeClassifier(max_depth=max_depth[i], min_samples_leaf = min_samples_leaves[j])

			for train_index, test_index in kf.split(X):
				X_train, X_test = X.ix[train_index], X.ix[test_index]
				y_train, y_test = y.ix[train_index], y.ix[test_index]

				model.fit(X_train, y_train)
				y_pred = model.predict(X_test)
					
				if i not in precision:
					precision[i] = {}
				if j not in precision[i]:
					precision[i][j] = 0

				if i not in recall:
					recall[i] = {}
				if j not in recall[i]:
					recall[i][j] = 0
				
				precision[i][j] += precision_score(y_pred, y_test, average='macro')
				recall[i][j] += recall_score(y_pred, y_test, average='macro')


	print('')
	row_format ="{:>25}" * (4)
	print(row_format.format('MaxDepth', ' MinSamplesLeaves', 'Precision', 'Recall'))
	print('')
	for i in range(len(max_depth)):
		for j in range(len(min_samples_leaves)):
			print( row_format.format(max_depth[i], min_samples_leaves[j] , round(precision[i][j]/10.0,2),  round(recall[i][j]/10.0, 2)))


if __name__ == "__main__":
	Q1()
	Q2()