# DS Practical 4
# Aim: Write a python program to perform Simple Linear Regression

# ============================================================
# 4A) Univariate Linear Regression - Predict Salary from Experience
# ============================================================

import numpy as np
# !pip install scikit-learn

from sklearn import datasets

# Generate synthetic regression dataset
x, y, coef = datasets.make_regression(
    n_samples=100,
    n_features=1,
    n_informative=1,
    noise=10,
    coef=True,
    random_state=0
)

# Scale x to represent Years of Experience (0 to 20)
x = np.interp(x, (x.min(), x.max()), (0, 20))
print(len(x))
print(x)

# Scale y to represent Salary (20000 to 150000)
y = np.interp(y, (y.min(), y.max()), (20000, 150000))
print(len(y))
print(y)

# Plot training data
import matplotlib.pyplot as plt

plt.plot(x, y, '.', label='training data')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.title('Experience vs Salary')
plt.show()

# Train Linear Regression model
from sklearn.linear_model import LinearRegression

reg_model = LinearRegression()
reg_model.fit(x, y)

# Predict
y_predicted = reg_model.predict(x)

# Plot training data and predicted regression line
plt.plot(x, y_predicted, '.', color="black", label="Predicted data")
plt.plot(x, y, '.', label="training data")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.title("Experience vs salary")
plt.legend()
plt.show()


# ============================================================
# 4B) Simulate Linear Model Y = 10 + 7*X + e for 100 random samples
# ============================================================

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

reg_model = LinearRegression()

x = np.random.rand(100, 1)
error = np.random.rand(100, 1)

b0 = 10
b1 = 7

y = b0 + b1 * x + error

reg_model.fit(x, y)
y_predicted = reg_model.predict(x)

plt.plot(x, y_predicted, '.', color="black", label="Predicted data")
plt.plot(x, y, '.', label="Training data")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("X vs Y")
plt.legend()
plt.show()


