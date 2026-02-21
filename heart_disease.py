import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
train = pd.read_csv('./data/train.csv')
test = pd.read_csv('./data/test.csv')

# load the data
test_ids = test['id']

# save the id column
print(test_ids.head(20))
print(f"\nNumber of rows in test_ids: {len(test_ids)}")

print("\nTraining Data:")
# Display the first few rows of the training data
print(train.head())

# Basic Data Inspection
print("\nData Info:")
print(train.info())

print("\nMissing Values:")
print(train.isnull().sum())

print("\nDuplicate Rows:")
print(train.duplicated().sum())

print("\nStatistical Summary:")
print(train.describe())

# Data Cleaning
# Drop the 'id' column as it is not needed for analysis
if 'id' in train.columns:
    train = train.drop('id', axis=1)
    print("\nDropped 'id' column.")

# Target Variable Analysis
plt.figure(figsize=(10, 6))
sns.countplot(x='Heart Disease', data=train)
plt.title('Distribution of Heart Disease')
plt.show()

# Numerical Features Analysis
numerical_features = ['Age', 'Max HR', 'Cholesterol', 'BP']
for feature in numerical_features:
    plt.figure(figsize=(10, 6))
    sns.histplot(train[feature], kde=True)
    plt.title(f'Distribution of {feature}')
    plt.show()

# Correlation Analysis
plt.figure(figsize=(12, 10))
# Calculate correlation matrix only for numeric columns
numeric_train = train.select_dtypes(include=[np.number])
sns.heatmap(numeric_train.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Categorical Features Analysis
categorical_features = ['Sex', 'Chest pain type', 'FBS over 120', 'EKG results', 'Exercise angina', 'Slope of ST', 'Number of vessels fluro', 'Thallium']
for feature in categorical_features:
    plt.figure(figsize=(10, 6))
    sns.countplot(x=feature, hue='Heart Disease', data=train)
    plt.title(f'{feature} Distribution by Heart Disease')
    plt.show()