# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:29:04 2020

@author: erick
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

df = pd.read_csv('dataset.csv')
df.drop(['id'], axis=1, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(df.drop(['risk'], axis=1), 
                                                    df['risk'], 
                                                    test_size=0.2, 
                                                    random_state=42)


NUMERICAL_FEATURES = ['age', 'job', 'credit_amount' ,'duration']
CATEGORICAL_FEATURES = ['sex', 'housing', 'saving_accounts', 'checking_account', 'purpose']

numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy="median")),
    ('scaler', StandardScaler())])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('numerical', numerical_transformer, NUMERICAL_FEATURES),
        ('categorical', categorical_transformer, CATEGORICAL_FEATURES)])

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('randomforest', RandomForestClassifier(random_state=27))])

model.fit(X_train, y_train)

predictions = model.predict(X_test)

output = predictions[0]

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

#Cross-Validation
from sklearn.model_selection import KFold, cross_validate, GridSearchCV
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
results = cross_validate(model, X=df.drop(['risk'], axis=1),y=df['risk'], cv=kfold)

#Grid Search
parameters = {'randomforest__max_depth': [3,4,5]}
grid = GridSearchCV(model, param_grid=parameters, cv=kfold)
grid.fit(X=df.drop(['risk'], axis=1), y=df['risk'])

grid.cv_results_
grid.best_params_
grid.best_score_
grid_results = pd.DataFrame(grid.cv_results_)

from sklearn import set_config
from sklearn.utils import estimator_html_repr

set_config(display='diagram')

with open('creditrisk.html', 'w') as f:
    f.write(estimator_html_repr(grid))




