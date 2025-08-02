

# 🔍 Customer Churn Prediction with Decision Tree

This project builds and evaluates a **Decision Tree Classifier** to predict customer churn using structured banking data. It includes **data preprocessing, model training**, and **visual performance evaluation** using various plots such as a **confusion matrix**, **correlation heatmap**, and **accuracy bar chart**.

---

## 📁 Dataset

The dataset used is `Churn_Modelling.csv`, which contains records of customers and whether they exited the bank (`Exited` = 1) or not (`Exited` = 0).

**Selected Features:**

* `CreditScore`
* `Age`
* `Tenure`
* `Balance`
* `NumOfProducts`
* `HasCrCard`
* `EstimatedSalary`

**Target Variable:**

* `Exited` (1 = churned, 0 = retained)

---

## 🧠 Project Workflow

### 1. 📦 Load and Prepare Data

* Load CSV using `pandas`
* Select relevant features for training
* Split the dataset into **training (70%)** and **testing (30%)** sets

### 2. 🌳 Train the Model

* Model: `DecisionTreeClassifier` from `scikit-learn`
* Trained on selected customer attributes

### 3. 📈 Evaluate the Model

* Predict churn status for test data
* Calculate accuracy using `accuracy_score`
* Visualize results:

  * 🔹 **Confusion Matrix**: Shows true vs predicted labels
  * 🔹 **Correlation Matrix**: Highlights relationships among features
  * 🔹 **Accuracy Bar Chart**: Displays overall model accuracy

---

## 📊 Visual Outputs

| Visualization            | Description                                       |
| ------------------------ | ------------------------------------------------- |
| `confusion_matrix.png`   | Annotated heatmap of prediction results           |
| `correlation_matrix.png` | Feature correlation to identify multicollinearity |
| `model_accuracy_bar.png` | Bar chart of model accuracy                       |

---

## 🧪 Requirements

Make sure the following libraries are installed:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

## 🚀 How to Run

1. Place `Churn_Modelling.csv` in your working directory.
2. Run the Python script to:

   * Train the decision tree model
   * Generate predictions
   * Visualize and save output plots

---

## 📌 Sample Output

```
Model Accuracy: 84.67%
```

> *(Output may vary depending on dataset split and random state)*


## 👨‍💻 Author

**MI**

