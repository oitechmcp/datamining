from sklearn.cluster import AgglomerativeClustering

X = [[22, 20], [25, 25], [28, 30], [40, 70], [42, 75], [45, 80]]
model = AgglomerativeClustering(n_clusters=2)
labels = model.fit_predict(X)
print("Clusters formed:", labels)
