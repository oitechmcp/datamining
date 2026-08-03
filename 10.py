import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
print("Cosine Similarity:", cos_sim)
