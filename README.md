# Heart Failure Prediction Project

## Description
This project aims to predict the likelihood of heart failure events based on clinical records. The dataset contains various features related to heart health, such as age, serum creatinine, ejection fraction, and more, to train machine learning models to predict whether a patient will experience heart failure. The dataset is obtained from [Kaggle](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data).

## Dataset
The dataset used for this project is the **Heart Failure Clinical Records Dataset**, which includes clinical records for patients with heart failure. The key target variable is `DEATH_EVENT`, where `1` represents a death event and `0` represents survival. The features in the dataset include continuous and categorical variables related to patient health.

## Requirements
To run the project, the following Python libraries are required:
- numpy
- pandas
- scikit-learn
- seaborn
- matplotlib

## Data Preprocessing
In this project, the dataset is preprocessed using the following steps:

1. **Data Loading**: The dataset is loaded into a Pandas DataFrame.
2. **Target Variable Separation**: The target variable (`DEATH_EVENT`) is separated from the features (input variables).
3. **Feature Scaling**: The features are standardized using **StandardScaler** to ensure that all the features are on the same scale.
4. **Train-Test Split**: The data is split into training and testing sets using an 80-20 ratio to evaluate model performance effectively.

## Data Analysis & Visualizations
In this project, various visualizations are performed to explore the relationships between different features in the dataset and their impact on predicting heart failure events. For a detailed analysis of each visualization and its interpretation, please refer to the [Analysis and Visualizations Report](docs/analysis_and_visualizations_report.pdf) file.

### Visualizations Include:
1. **Correlation Heatmap**: Correlations between features in the dataset.
2. **Scatterplot**: Visualizing `Age` vs `Serum Creatinine`.
3. **Histogram**: Distribution of `Age`.
4. **Boxplot**: Relationship between `Ejection Fraction` and `DEATH_EVENT`.
5. **Barplot**: Gender and Age distribution with respect to death events.
6. **Lineplot**: Trends of `Serum Sodium` over time.

These visualizations help to better understand the dataset and guide the choice of machine learning models.

## Model Training & Evaluation
In this project, multiple machine learning models are trained and evaluated to predict heart failure events based on various features in the dataset. The following models are used:

1. **Naive Bayes**
2. **K-Nearest Neighbors (KNN)**
3. **Decision Tree**
4. **Random Forest**

Each model is evaluated using metrics such as accuracy, precision, recall, and confusion matrix. For a detailed explanation of the model performance, including metrics and comparison between different models, please refer to the [Model Evaluation Report](docs/model_evaluation_report.pdf) file.

### Evaluation Metrics Include:
- **Accuracy**: Overall correctness of the model.
- **Confusion Matrix**: Breakdown of predicted vs actual values.
- **Precision**: Measure of correctly predicted positive observations.
- **Recall**: Measure of correctly predicted positive observations out of actual positives.

These metrics help assess which model performs best in predicting heart failure events.

## Example Output
Naive Bayes:
Accuracy: 85%
Precision: 84%
Recall: 87%
Confusion Matrix: [[85, 10], [12, 63]]

Random Forest:
Accuracy: 88%
Precision: 86%
Recall: 90%
Confusion Matrix: [[92, 5], [9, 61]]

## Conclusion
Based on the evaluation metrics, the Random Forest classifier performs the best for this dataset in terms of both precision and recall. The model demonstrates a good ability to predict death events, which could assist in healthcare decision-making.
