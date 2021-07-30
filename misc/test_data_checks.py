import pandas as pd
import pytest

from pandas_summary import DataFrameSummary
# import yaml


def check_schema(df, columns):
    for col in df.columns:
        assert col in columns, f'"{col}" not in data column specification'

def test_budget_schemas():
    # metadata = yaml.load('data/metadata_budget.yml')
    # dump = yaml.dump(metadata)['columns']
    # columns = dump['columns']
    columns = ["PassengerId", "Survived", "Pclass", "Name", "Sex",
                "Age", "SibSp", "Parch", "Ticket", "Fare","Embarked"]
    df = pd.read_csv('../data/clean/clean_train.csv')
    check_schema(df, columns)

def check_data_completeness(df):
    df_summary =DataFrameSummary(df).summary()
    for col in df_summary.columns:
        assert df_summary.loc['missing', col] == 0, f'{col} has missing values'

def test_missing_values_dataset():
    df = pd.read_csv('../data/clean/clean_train.csv')
    check_data_completeness(df)