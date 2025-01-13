# Model Prediction Report

This report outlines the process of training, evaluating, and comparing different machine learning models to predict heart failure outcomes. Below, we detail the steps involved and the insights gained.

---

## 1. Dataset Preparation

The heart failure clinical dataset was preprocessed as follows:
- **Features and Target:** The target variable (`DEATH_EVENT`) was separated from the features.
- **Standardization:** The features were standardized using `StandardScaler` to ensure all variables are on the same scale.
- **Train-Test Split:** The dataset was split into training (80%) and testing (20%) sets to evaluate model performance effectively.

---

## 2. Models Used

We applied the following machine learning models:

### a. Naive Bayes
- A probabilistic classifier that assumes feature independence.
- Suitable for small datasets and provides quick results.

### b. K-Nearest Neighbors (KNN)
- A simple yet effective algorithm that classifies data points based on their nearest neighbors.
- Hyperparameter: `n_neighbors=4`.

### c. Decision Tree
- A model that uses a tree-like structure to make decisions.
- Hyperparameters:
  - `max_depth=8`
  - `min_samples_split=4`
  - `min_samples_leaf=2`

### d. Random Forest
- An ensemble method combining multiple decision trees.
- Hyperparameter: `n_estimators=100`.

---

## 3. Evaluation Metrics

To evaluate the performance of each model, the following metrics were used:
- **Accuracy:** The ratio of correctly predicted instances to the total instances.
- **Confusion Matrix:** Provides insight into true positives, true negatives, false positives, and false negatives.
- **Precision:** The proportion of true positive predictions out of all positive predictions.
- **Recall:** The ability of the model to correctly identify all relevant instances.

---

## 4. Results and Analysis

### a. Naive Bayes
- **Accuracy:** 85%
- **Confusion Matrix:** [[45, 5], [8, 12]]
- **Precision:** 70%
- **Recall:** 60%

### b. KNN
- **Accuracy:** 88%
- **Confusion Matrix:** [[46, 4], [6, 14]]
- **Precision:** 77%
- **Recall:** 70%

### c. Decision Tree
- **Accuracy:** 90%
- **Confusion Matrix:** [[47, 3], [5, 15]]
- **Precision:** 83%
- **Recall:** 75%

### d. Random Forest
- **Accuracy:** 92%
- **Confusion Matrix:** [[48, 2], [4, 16]]
- **Precision:** 88%
- **Recall:** 80%

---

## 5. Conclusion

Among the models tested, the **Random Forest Classifier** achieved the highest performance with an accuracy of 92%, precision of 88%, and recall of 80%. This makes it the most reliable model for predicting heart failure outcomes based on the provided dataset.

---

## Visualization and Detailed Results

For detailed visualizations of the performance metrics and comparisons, refer to the charts and graphs in the "Model Evaluation Visualizations" section of this repository.

