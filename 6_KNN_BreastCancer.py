# DS Practical 5
# Aim: Write a python program to implement KNN algorithm
#      to predict Breast Cancer using Breast Cancer Wisconsin dataset.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns

sns.set()

# Load dataset
breast_cancer_data = load_breast_cancer()

# Create feature DataFrame
X_df = pd.DataFrame(breast_cancer_data.data, columns=breast_cancer_data.feature_names)
X_df.head()

X_df.info()

# Select only 2 features for visualization
X_df = X_df[['mean area', 'mean compactness']]
X_df.head()

X_df.info()

# Create target variable
Y_df = pd.Categorical.from_codes(breast_cancer_data.target, breast_cancer_data.target_names)
print(Y_df)

# Encode target as dummy variable (drop first to avoid dummy trap)
Y_df = pd.get_dummies(Y_df, drop_first=True)
Y_df.info()

print(Y_df)

# Split into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(
    X_df, Y_df, random_state=1, test_size=0.25, shuffle=True
)

X_test.info()
Y_test.info()

X_train.info()
Y_train.info()

# Build KNN model
knn = KNeighborsClassifier(n_neighbors=5, metric="euclidean")
knn.fit(X_train, Y_train)

# Scatter plot: Actual classes
combined_df = pd.concat([X_test, Y_test], axis=1)
sns.scatterplot(x="mean area", y="mean compactness", hue="benign", data=combined_df)
plt.show()

# Predict
Y_pred = knn.predict(X_test)

# Scatter plot: Predicted classes
plt.scatter(X_test["mean area"], X_test["mean compactness"], c=Y_pred)
plt.show()

# Confusion Matrix
cf = confusion_matrix(Y_test, Y_pred)
print(cf)

tp, fn, fp, tn = confusion_matrix(Y_test, Y_pred, labels=[1, 0]).reshape(-1)
print(tp, fn, fp, tn)

# Heatmap of Confusion Matrix
ax = plt.subplot()
sns.heatmap(cf, annot=True, ax=ax)
ax.set_xlabel("Predicted Values")
ax.set_ylabel("Actual Values")
ax.set_title("Confusion Matrix")
ax.xaxis.set_ticklabels(["Malignant", "Benign"])
ax.yaxis.set_ticklabels(["Malignant", "Benign"])
plt.show()

# Evaluation Metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

accuracy  = accuracy_score(Y_test, Y_pred)
precision = precision_score(Y_test, Y_pred)
recall    = recall_score(Y_test, Y_pred)
f1        = f1_score(Y_test, Y_pred)

print("Accuracy:",  accuracy)
print("Precision:", precision)
print("Recall:",    recall)
print("F1-score:",  f1)
