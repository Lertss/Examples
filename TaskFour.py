# Creating hierarchical clustering of iris data

from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn import datasets
import matplotlib.pyplot as plt

fret = plt.figure(figsize=(15, 30))
fret.patch.set_facecolor('white')

iris = datasets.load_iris()
gings = linkage(iris.data, method='ward')

rert = dendrogram(gings, labels=[iris.target_names[i] for i in iris.target], orientation='left', leaf_font_size=12)
plt.show()
