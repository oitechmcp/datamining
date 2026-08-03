import numpy as np

data = [12, 14, 15, 16, 17, 18, 19, 22, 95]
q1, q3 = np.percentile(data, [25, 75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
outliers = [x for x in data if x < lower or x > upper]
print("Outliers:", outliers)
