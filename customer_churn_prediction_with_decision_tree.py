# -*- coding: utf-8 -*-
"""Customer Churn Prediction with Decision Tree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CpX-c6RfUCbquUeiS-RVdOt9L6peItqD
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

# Load dataset
dataset = pd.read_csv('Churn_Modelling.csv')

# Prepare features and target
X = dataset[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'EstimatedSalary']]
y = dataset['Exited']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Train Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred) * 100

# Visualization 1: Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Non-Churned (0)', 'Churned (1)'],
            yticklabels=['Non-Churned (0)', 'Churned (1)'])
plt.title('Confusion Matrix', fontsize=16)
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.tight_layout()
plt.savefig('confusion_matrix.png')
plt.show()

# Visualization 2: Correlation Matrix
plt.figure(figsize=(10, 8))
corr_matrix = X.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f',
            square=True, linewidths=0.5)
plt.title('Correlation Matrix of Features', fontsize=16)
plt.tight_layout()
plt.savefig('correlation_matrix.png')
plt.show()

# Visualization 3: Accuracy Bar Chart
plt.figure(figsize=(6, 8))
sns.barplot(x=['Decision Tree Classifier'], y=[accuracy], hue=['Decision Tree Classifier'], palette=['#36A2EB'])
plt.ylim(0, 100)
plt.ylabel('Accuracy (%)', fontsize=12)
plt.title('Model Accuracy', fontsize=16)
plt.tight_layout()
plt.savefig('model_accuracy_bar.png')
plt.show()

print(f"Model Accuracy: {accuracy:.2f}%")