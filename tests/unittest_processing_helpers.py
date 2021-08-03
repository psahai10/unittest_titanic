import unittest
import numpy as np

class TestClass(unittest.TestCase):
    # https://www.geeksforgeeks.org/python-unittest-assertisinstance-function/
    def test_get_df(self):
        df = get_df(file_path)
        expected = pd.DataFrame()
        self.assertIsInstance(df, expected, "given object is not a pandas data frame")

    def test_missing_values(df):
        missing_values = missing_values(df)
        self.assertIsInstance(type(missing_values), pd.Series, "Incorrect output when checking missing values")
        self.assertEqual(str(missing_values.dtypes, "dtype('int64')", "Incorrect dtypes when checking missing value")

    def test_perc_missing_values(df):
        perc_missing_value = list(perc_missing_values(df))
        for val in perc_missing_value:
            self.assertTrue(0 <= val <= 100)

    def test_columns_dtype(df):
        expected_types = [np.dtype("int64"), np.dtype(object), np.dtype("float64")]
        val_types = list(df.dtypes)
        for types in val_types:
            self.assertTrue(types in expected_types)

    def test_missing_values_table_info(df):
        summary_df = missing_values_table_info(df)
        expected_instance = pd.DataFrame()
        expected_columns = ['Missing Values', '% of Total Values', 'Data Types']
        self.assertIsInstance(summary_df, expected_instance, "given output is not a pandas data frame")
        self.assertEqual(list(summary_df.columns), expected_columns, 'Incorrect input for summary table')

    def test_clean_df_cols_missing_values(summary_df):
        threshold_0 = clean_df_cols_missing_values(summary_df, 0)
        threshold_10 = clean_df_cols_missing_values(summary_df, 10)
        threshold_20 = clean_df_cols_missing_values(summary_df, 20)
        threshold_80 = clean_df_cols_missing_values(summary_df, 80)
        self.assertEqual(threshold_0, ['Cabin', 'Age', 'Embarked'])
        self.assertEqual(threshold_10, ['Cabin', 'Age'])
        self.assertEqual(threshold_20, ['Cabin'])
        self.assertEqual(threshold_80, [])
    
    def test_drop_cols(df, cols):
        test_cols_1= ["PassengerId", "Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"]
        drop_1 = []
        test_cols_2= ["PassengerId", "Pclass","Sex","SibSp","Parch","Fare","Cabin"]
        drop_2 = ["Survived","Name","Age","Ticket","Embarked"]
        df1 = drop_cols(df, drop_1)
        df2 = drop_cols(df, drop_2)
        self.assertEqual(df1.columns, test_cols_1)
        self.assertEqual(df2.columns, test_cols_2)

if __name__ == '__main__':
    unittest.main()