
# Md Lutfar Rahman
# mrahman9@memphis.edu
# DataScience Assingment - 4

import pandas
import seaborn
from matplotlib import pyplot

from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics import silhouette_score
df = pandas.read_csv('Sales_Transactions_Dataset_Weekly.csv')

def Q1():
	from sklearn.cluster import KMeans
	Ws = [ 'W' + str(i) for i in range(51)]
	#print(Ws)
	XW = df[Ws]
	mW = KMeans(n_clusters=3)
	mW.fit(XW)
	print('Using Ws:', adjusted_rand_score(df.W51, mW.labels_))

	Normalizeds = [ 'Normalized ' + str(i) for i in range(51)]
	#print(Normalizeds)
	XW = df[Normalizeds]
	mNormalized = KMeans(n_clusters=3)
	mNormalized.fit(XW)
	print('Using Normalizeds:', adjusted_rand_score(df['Normalized 51'], mNormalized.labels_))


from kmeans import Point, Cluster, KMeans
import random

#-----------------------------------------------------------
def silhouette(points, clusters):
	s = [0] * len(points)
	for i, p in enumerate(points):
		b_min = None
		for c in clusters:
			if p in c.points:
				a, a_count = 0, 0
				for q in c.points:
					a += p.RMS(q)
					a_count += 1
				a = a/a_count
			else:
				b, b_count = 0, 0
				for q in c.points:
					b += p.RMS(q)
					b_count += 1
				b = b/b_count
				if b_min is None or b_min > b:
					b_min = b

		# print(a, b_min)
		s[i] = (b_min-a)/max(b_min,a)
	return sum(s)/len(s)


#-----------------------------------------------------------
def get_data():
	file_name = 'Sales_Transactions_Dataset_Weekly.csv'
	with open(file_name) as f:
		header = f.readline()
		points = []
		for line in f:
			items = line.strip().split(',')
			r = [float(item) for item in items[1:]]
			points.append( Point(r) )
	random.shuffle(points)
	return points
#-----------------------------------------------------------

points = get_data()
features = range(52)
Point.set_features(*features)
thres = 0.01


def Q2():
	for k in range(2, 10):
		model = KMeans(points, k, thres)
		model.cluster()
		# model.show()
		print('k = ', k, 'silhouette = ', silhouette(model.points, model.clusters))



def Q3():
	k=2
	model = KMeans(points, k, thres)
	model.cluster()

	min_sil = None
	min_sil_cluster = None
	for c in model.clusters:
		sil = silhouette(c.points, model.clusters)
		if min_sil is None or min_sil > sil:
			min_sil = sil 
			min_sil_cluster = c


	print('')
	print('Minimum silhoutte cluster details:')
	print('minimun silhoutte:', min_sil)
	print('# points: ', len(min_sil_cluster.points))
	print('Cluster Centroid:',min_sil_cluster.centroid)



def Q4():
	k=2
	model = KMeans(points, k, thres)
	model.cluster()

	max_sil = None
	max_sil_cluster = None
	for c in model.clusters:
		sil = silhouette(c.points, model.clusters)
		if max_sil is None or max_sil < sil:
			max_sil = sil 
			max_sil_cluster = c


	print('')
	print('Maximum silhoutte cluster details:')
	print('Maximum silhoutte:', max_sil)
	print('# points: ', len(max_sil_cluster.points))
	print('Cluster Centroid:',max_sil_cluster.centroid)

