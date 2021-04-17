from processors.transformers import numerical_transformer, categorical_transformer
from sklearn.compose import ColumnTransformer
from instances import config

preprocessor = ColumnTransformer(
    transformers=[
        ('numerical', numerical_transformer, config.NUMERICAL_FEATURES),
        ('categorical', categorical_transformer, config.CATEGORICAL_FEATURES)])
