import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class DataMissing(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None) -> None:
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> "CategoricalImputer":
        """Fit statement to accomodate the sklearn pipeline."""

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Apply the transforms to the dataframe."""

        X = X.fillna(value='no_data')
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna("Missing")

        return X
