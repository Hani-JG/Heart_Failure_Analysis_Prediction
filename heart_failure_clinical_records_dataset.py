import numpy as np
import pandas as pd
df = pd.read_csv('./heart_failure_clinical_records_dataset.csv')

x = df.drop('DEATH_EVENT', axis= 1)
y = df['DEATH_EVENT']

x = np.array(x)
y = np.array(y)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x = scaler.fit_transform(x)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size= 0.2)

import seaborn as sns
import matplotlib.pyplot as plt


correlation_matrix = df.corr()


plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix for Heart Failure Dataset')
plt.show()

sns.scatterplot(x='age', y='serum_creatinine', hue='DEATH_EVENT', data=df)
plt.title('Age vs Serum Creatinine - Heart Failure')
plt.show()

sns.histplot(df['age'], kde=True, bins=30)
plt.title('Age Distribution - Heart Failure')
plt.show()

sns.boxplot(x='DEATH_EVENT', y='ejection_fraction', data=df)
plt.title('Ejection Fraction vs Death Event')
plt.show()

sns.barplot(x='sex', y='age', hue='DEATH_EVENT', data=df)
plt.title('Gender vs Age - Heart Failure')
plt.show()

sns.lineplot(x='time', y='serum_sodium', data=df)
plt.title('Serum Sodium Over Time')
plt.show()

df['DEATH_EVENT'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Death Event Distribution')
plt.ylabel('')
plt.show()


def calculate_metrics(y_test, y_pred):
    from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
    acc = accuracy_score(y_test,y_pred)
    conf = confusion_matrix(y_test, y_pred)
    p = precision_score(y_test, y_pred)
    r = recall_score(y_test, y_pred)
    return {
    'accuracy': acc,
        'confusion_matrix': conf,
        'precision': p,
        'recall': r
    }

def naive_bayes(x_train, y_train,x_test, y_test):
    from sklearn.naive_bayes import GaussianNB
    model = GaussianNB()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    metrics = calculate_metrics(y_test, y_pred)
    print('accuracy NB =', metrics['accuracy'])
    print('confusion matrix NB =', metrics['confusion_matrix'])
    print('precision score NB =', metrics['precision'])
    print('recall score NB =', metrics['recall'])

def KNN(x_train, y_train,x_test, y_test):
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors= 4)
    knn.fit(x_train,y_train)
    y_pred = knn.predict(x_test)
    metrics = calculate_metrics(y_test, y_pred)
    print('accuracy KNN =', metrics['accuracy'])
    print('confusion matrix KNN =', metrics['confusion_matrix'])
    print('precision score KNN =', metrics['precision'])
    print('recall score KNN =', metrics['recall'])

def Decision_Tree(x_train, y_train,x_test, y_test):
    from sklearn.tree import DecisionTreeClassifier
    dt = DecisionTreeClassifier(max_depth= 8, min_samples_split= 4, min_samples_leaf= 2)
    dt.fit(x_train, y_train)
    y_pred = dt.predict(x_test)
    metrics = calculate_metrics(y_test, y_pred)
    print('accuracy DT =', metrics['accuracy'])
    print('confusion matrix DT =', metrics['confusion_matrix'])
    print('precision score DT =', metrics['precision'])
    print('recall score DT =', metrics['recall'])

def Random_Forest(x_train, y_train,x_test, y_test):
    from sklearn.ensemble import RandomForestClassifier
    rf = RandomForestClassifier(n_estimators= 100)
    rf.fit(x_train, y_train)
    y_pred = rf.predict(x_test)
    metrics = calculate_metrics(y_test, y_pred)
    print('accuracy RF =', metrics['accuracy'])
    print('confusion matrix RF =', metrics['confusion_matrix'])
    print('precision score RF =', metrics['precision'])
    print('recall score Rf =', metrics['recall'])

naive_bayes(x_train, y_train,x_test, y_test)
KNN(x_train, y_train,x_test, y_test)
Decision_Tree(x_train, y_train,x_test, y_test)
Random_Forest(x_train, y_train,x_test, y_test)

