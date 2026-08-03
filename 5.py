from sklearn.neighbors import KNeighborsClassifier

X = [[20], [25], [35], [45], [55], [65]]
y = ["Low", "Low", "Medium", "Medium", "High", "High"]

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
print("Predicted Class:", knn.predict([[40]])[0])
