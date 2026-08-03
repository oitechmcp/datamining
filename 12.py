from sklearn.linear_model import LinearRegression

X = [[1200], [1500], [1800], [2100], [2400]]
y = [48, 60, 72, 84, 96]

model = LinearRegression()
model.fit(X, y)
print("Predicted Price for 2000 sq.ft:", model.predict([[2000]])[0])
