# DS Practical 6
# Aim: Perform Decision Tree algorithm on train.csv (Titanic dataset)

import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
titanic_df = pd.read_csv("train.csv")
titanic_df.info()

# Select features
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
x = titanic_df[features]
x.info()

# Target variable
Y = titanic_df['Survived']
Y.info()

# Encode 'Sex' column: male -> 0, female -> 1
x['Sex'] = x['Sex'].map({'male': 0, 'female': 1})
x.head()

# Fill missing Age values with median
x['Age'].fillna(x['Age'].median(), inplace=True)

# Verify no null values remain
x.isnull().sum()

# Split dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    x, Y, test_size=0.2, random_state=10
)

# Build Decision Tree model
dtmodel = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=10)
dtmodel.fit(X_train, Y_train)

# Predict
Y_pred = dtmodel.predict(X_test)

# Accuracy and Classification Report
print("Accuracy: ", accuracy_score(Y_test, Y_pred))
print(classification_report(Y_test, Y_pred))

# Visualize the Decision Tree
plt.figure(figsize=(18, 10))
plot_tree(
    dtmodel,
    feature_names=features,
    class_names=['Not Survived', 'Survived'],
    filled=True
)
plt.show()
