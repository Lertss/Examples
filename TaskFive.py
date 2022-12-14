#Implementation of the K-Means algorithm.

from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()
mod = KMeans(n_clusters=3, n_init=10)
mod.fit(iris.data)
predicted = mod.predict([[7.2, 3.5, 0.8, 1.6, ]])
all_predicted = mod.predict(iris.data)

print("Predictions on a single example: ", predicted)

print("Forecasting for the entire data set: \n", all_predicted)