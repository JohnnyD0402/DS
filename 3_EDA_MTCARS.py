# DS Practical 3
# Aim: Exploratory Data Analysis of mtcars.csv Dataset in Python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("mtcars.csv")

# Display first 5 rows
df.head()

# Dataset info
df.info()

# Statistical summary
df.describe()

# Check for null values
df.isnull().sum()

# Mean MPG grouped by number of cylinders
df.groupby("cyl")["mpg"].mean()

# Gear value counts
df["gear"].value_counts()

# Import visualization libraries
import seaborn as sns
import plotly.express as px

sns.set(style="whitegrid")

# Pairplot of all numeric columns
sns.pairplot(
    df.drop(columns=["model"]),
    diag_kind="kde",
    corner=True
)
plt.suptitle("Seaborn Pairplot of MTCARS Dataset", y=1.02)
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(
    df.drop(columns=["model"]).corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap (Seaborn)")
plt.show()

# Boxplot: MPG vs Cylinders
plt.figure(figsize=(8, 5))
sns.boxplot(x="cyl", y="mpg", data=df)
plt.title("MPG vs Cylinders")
plt.show()

# Boxplot: MPG vs Transmission (0=Auto, 1=Manual)
plt.figure(figsize=(8, 5))
sns.boxplot(x="am", y="mpg", data=df)
plt.title("MPG vs Transmission (0=Auto, 1=Manual)")
plt.show()

# Boxplot: MPG vs Gears
plt.figure(figsize=(8, 5))
sns.boxplot(x="gear", y="mpg", data=df)
plt.title("MPG vs Gears")
plt.show()

# Violin Plot: MPG vs Cylinders
plt.figure(figsize=(8, 5))
sns.violinplot(x="cyl", y="mpg", data=df)
plt.title("Violin Plot: MPG vs Cylinders")
plt.show()

# Violin Plot: MPG vs Transmission
plt.figure(figsize=(8, 5))
sns.violinplot(x="am", y="mpg", data=df)
plt.title("Violin Plot: MPG vs Transmission")
plt.show()

# Regression Plot: MPG vs Weight
sns.lmplot(x="wt", y="mpg", data=df, height=5, aspect=1.3)
plt.title("Regression: MPG vs Weight")
plt.show()

# Regression Plot: MPG vs Horsepower
sns.lmplot(x="hp", y="mpg", data=df, height=5, aspect=1.3)
plt.title("Regression: MPG vs Horsepower")
plt.show()

# Interactive Scatter: MPG vs Weight (colored by cyl, sized by hp)
fig = px.scatter(
    df,
    x="wt",
    y="mpg",
    color="cyl",
    size="hp",
    hover_name="model",
    title="Interactive MPG vs Weight"
)
fig.show()

# Interactive Scatter: MPG vs Horsepower (colored by am)
fig = px.scatter(
    df,
    x="hp",
    y="mpg",
    color="am",
    hover_name="model",
    title="Interactive MPG vs Horsepower"
)
fig.show()
