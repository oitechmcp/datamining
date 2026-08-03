from sklearn.tree import DecisionTreeClassifier, export_text

X = [[25000, 22], [30000, 25], [35000, 30], [50000, 35], [60000, 40], [70000, 45]]
y = ["Reject", "Reject", "Reject", "Approve", "Approve", "Approve"]

clf = DecisionTreeClassifier()
clf.fit(X, y)
print(export_text(clf, feature_names=["Income", "Age"]))
