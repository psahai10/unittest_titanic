from data import *
import pytest
import numpy
import pandas as pd
from unittest.mock import patch, Mock


@patch('data.raw.train.pandas.read_csv')
def test_get_df(read_csv_mock: Mock):

    read_csv_mock.return_value = pd.DataFrame({
                    "PassengerId": [1,2,3,4,5],
                    "Survived": [0,1,1,1,0],
                    "Pclass": [3,1,3,1,3],
                    "Name": ['John', 'Maria', 'Ali', 'Allen', 'Joe'],
                    "Sex": ['male', 'female', 'femail', 'female', 'male'],
                    "Age": [22.0, 38.0, 26.0, 35.0, 35.0],
                    "SibSp": [1,1,0,1,0],
                    "Parch": [0,0,0,0,0],
                    "Ticket": ['A/5 21171', 'PC 17599', 'STON/O2. 3101282', '113803', '373450'],
                    "Fare": [7.2500, 71.2833, 7.9250, 53.1000, 8.0500],
                    "Cabin": ['NaN', 'C85', 'NaN', 'C123', 'NaN'],
                    "Embarked": ['S', 'C', 'S', 'S', 'S']
    })
    results = get_df()
    read_csv_mock.assert_called_once()

    pd.testing.assert_frame_equal(results, pd.DataFrame({
                    "PassengerId": [1,2,3,4,5],
                    "Survived": [0,1,1,1,0],
                    "Pclass": [3,1,3,1,3],
                    "Name": ['John', 'Maria', 'Ali', 'Allen', 'Joe'],
                    "Sex": ['male', 'female', 'femail', 'female', 'male'],
                    "Age": [22.0, 38.0, 26.0, 35.0, 35.0],
                    "SibSp": [1,1,0,1,0],
                    "Parch": [0,0,0,0,0],
                    "Ticket": ['A/5 21171', 'PC 17599', 'STON/O2. 3101282', '113803', '373450'],
                    "Fare": [7.2500, 71.2833, 7.9250, 53.1000, 8.0500],
                    "Cabin": ['NaN', 'C85', 'NaN', 'C123', 'NaN'],
                    "Embarked": ['S', 'C', 'S', 'S', 'S']
    }))