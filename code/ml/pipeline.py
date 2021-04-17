from sklearn.pipeline import Pipeline
from processors.preprocessors import preprocessor
from sklearn.ensemble import RandomForestClassifier

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('randomforest', RandomForestClassifier(random_state=27))])
