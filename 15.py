from sklearn.cluster import KMeans
import numpy as np

X = np.array([[22, 20], [25, 25], [28, 30], [40, 70], [42, 75], [45, 80]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print("Clusters:", kmeans.labels_)
