# ============================================================
# Multi-variate Linear Regression - Boston Housing Dataset
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
# !pip install scikit-learn

boston_df = pd.read_csv("Boston.csv")
boston_df.head()

boston_df.info()

# Drop unnamed index column
boston_df = boston_df.drop("Unnamed: 0", axis=1)

boston_df.info()

# Separate features and target
boston_x = pd.DataFrame(boston_df.iloc[:, :13])
boston_y = pd.DataFrame(boston_df.iloc[:, -1])

# Split into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(boston_x, boston_y, test_size=0.3)

print(f'X Train Size: {X_train.shape}')
print(f'X Test Size: {X_test.shape}')
print(f'Y Train Size: {Y_train.shape}')
print(f'Y Test Size: {Y_test.shape}')

# Train Linear Regression model
from sklearn.linear_model import LinearRegression

reg_model = LinearRegression()
reg_model.fit(X_train, Y_train)

# Predict on test set
y_predicted = reg_model.predict(X_test)

# Display predictions
Y_pred = pd.DataFrame(y_predicted, columns=["Predicted_Y"])
Y_pred.head()

# Scatter plot: Actual vs Predicted
plt.scatter(Y_test, Y_pred, c="green")
plt.xlabel("Actual Price(medv)")
plt.ylabel("Predicted Price")
plt.show()
