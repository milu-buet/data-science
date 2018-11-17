import math
import pandas

def Entropy(df, outcome, condition=None):
	if condition is not None:
		df = df[ condition ]
	outcomes = df[outcome].value_counts()
	total = sum(outcomes.values)
	probs = [ v/total for v in outcomes.values ]
	E = 0
	for p in probs:
		if p > 0:
			E += p * math.log2(1.0 / p)
	print('Values:', outcomes.values, 'Probs:', probs, 'Entropy:', E)
	return E


# df = pandas.read_csv('DecisionTreeExampleData.csv')
# print(Entropy(df, 'Outcome'))
# print(Entropy(df, 'Outcome', df.Where == 'Home'))
# print(Entropy(df, 'Outcome', df.Where == 'Away'))

# print(Entropy(df, 'Outcome', df.When == '5pm'))
# print(Entropy(df, 'Outcome', df.When == '7pm'))
# print(Entropy(df, 'Outcome', df.When == '9pm'))


# df = pandas.read_csv('~/Dropbox/datasets/admission.csv')
# print(Entropy(df, 'admit'))
# print(Entropy(df, 'admit', df.gpa < 3))
