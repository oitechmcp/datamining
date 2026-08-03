from sklearn.naive_bayes import GaussianNB

X = [[2], [3], [4], [5], [6], [7]]
y = ["Fail", "Fail", "Pass", "Pass", "Pass", "Pass"]

model = GaussianNB()
model.fit(X, y)
print("Prediction for 4.5 hours:", model.predict([[4.5]])[0])
print("Accuracy:", model.score(X, y))
