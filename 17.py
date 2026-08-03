from sklearn.cluster import BisectingKMeans

X = [[22, 20], [25, 25], [28, 30], [40, 70], [42, 75], [45, 80]]
model = BisectingKMeans(n_clusters=2, random_state=0).fit(X)
print("Divisive Clusters:", model.labels_)
