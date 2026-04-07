# DS Practical 2
# Aim: Exploratory Data Analysis (on Titanic train.csv dataset)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.getcwd()

os.chdir('Downloads')   # Change to the folder where train.csv is located

df = pd.read_csv("train.csv")

# Display first 5 rows
df.head()

# Dataset info
df.info()

# Statistical summary
df.describe()

# Check for null values
df.isnull().sum()

# Drop unnecessary columns
cleaned = df.drop(['PassengerId', 'Name', 'Ticket', 'Fare', 'Cabin'], axis=1)

cleaned.head()

# Fill missing Age with mean grouped by Pclass
cleaned['Age'] = cleaned['Age'].fillna(cleaned.groupby("Pclass")['Age'].transform("mean"))

# Check nulls after filling
cleaned.isnull().sum()

# Plot: Survival count by Sex
sns.catplot(x="Sex", hue="Survived", kind="count", data=cleaned)
plt.show()

# Group by Sex and Survived
cleaned.groupby(['Sex', 'Survived'])['Survived'].count()

group1 = cleaned.groupby(['Sex', 'Survived'])
gender_survived = group1.size().unstack()

# Heatmap: Gender vs Survived
sns.heatmap(gender_survived, annot=True, fmt="d")
plt.show()

# Heatmap: Pclass vs Survived
group2 = cleaned.groupby(['Pclass', 'Survived'])
pclass_survived = group2.size().unstack()
sns.heatmap(pclass_survived, annot=True, fmt="d")
plt.show()

# Violin plot: Age vs Sex colored by Survived
sns.violinplot(x="Sex", y="Age", hue="Survived", data=cleaned, split=True)
plt.show()

# Correlation matrix (drop non-numeric columns)
cleaned_corr = cleaned.drop(['Sex', 'Embarked'], axis=1)
cleaned_corr.corr(method="pearson")

# Heatmap of correlation
sns.heatmap(cleaned_corr.corr(method="pearson"), annot=True, vmax=1)
plt.show()
