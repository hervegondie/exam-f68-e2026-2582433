import numpy as np
from sklearn.linear_model import LinearRegression

# Inițializăm modelul și îl antrenăm cu date fictive
X_train = np.array([[1], [2], [3], [4]])
y_train = np.array([2, 4, 6, 8])  # y = 2 * x

model = LinearRegression()
model.fit(X_train, y_train)

def predict(features):
    """Primiți o listă de caracteristici și returnați predicția."""
    features = np.array(features).reshape(-1, 1)
    return model.predict(features).tolist()