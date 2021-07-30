import pandas as pd
import numpy as np
import os.path 

class ProcessRawCSV(object):

    def get_df(self, file_path):
        self.df = pd.read_csv(file_path)
        return self

    def missing_values_info(self, df):
        # Total missing values
        return df.isnull().sum()

    def perc_missing_values(self, df):
        # Percentage of missing values
        return 100 * df.isnull().sum() / len(df)

    def columns_dtypes(self, df):
        # Coumn for dtypes
        return df.dtypes

    def missing_values_table_info(self):
        mis_val = self.missing_values_info(self.df)
        mis_val_percent = self.perc_missing_values(self.df)
        dtype = self.columns_dtypes(self.df)
        # Make a table with the results
        mis_val_table = pd.concat([mis_val, mis_val_percent,dtype], axis=1)
        # Rename the columns
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values', 2:'Data Types'})
        # Sort the table by percentage of missing descending
        self.missing_vals = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        return self

    def clean_df_cols_missing_values(self, threshold=75):
        self.cols_to_drop = self.missing_vals[self.missing_vals["% of Total Values"]>threshold].index.tolist()
        return self

    def drop_cols(self):
        self.df.drop(columns=self.cols_to_drop)
        return self

    def clean_df_rows_missing_values(self):
        self.df.dropna()
        return self

    def cols_to_impute(self, df, _min=0, _max=25):
        min_cols_to_impute = df[df["% of Total Values"] >= _min].index.tolist()
        max_cols_to_impute = df[df["% of Total Values"] <= _max].index.tolist()
        self.cols_to_impute = list(set(min_cols_to_impute ) and set(max_cols_to_impute))
        return self

    def filter_by_dtypes(self, df, lst):
        self.nums, self.not_nums = [], []
        dtypes_list = self.df[self.cols_to_impute].dtypes.tolist() 
        for col, types in zip(self.cols_to_impute, dtypes_list):
            if types in ['float', 'int']:
                self.nums.append(col)
            else:
                self.not_nums.append(col)
        return self

    def imput(self):
        if self.nums:
            for col in self.nums:
                value = self.df[col].mean()
                self.df[col].fillna(value, inplace=True)
        return self

    file_name = '../data/clean/clean_train.csv'

    def save_csv(self, file_name):
        self.df.to_csv(file_name)


df_object = ProcessRawCSV()
df_object.get_df('../data/raw/train.csv')
df_object.missing_values_table_info(self.df)
df_object.clean_df_cols_missing_values(self.mis_val_table_ren_columns)

file_name = '../data/raw/train.csv'
df = pd.read_csv(file_name)
missing_values_summary = missing_values_table_info(df)
cols_to_drop = clean_df_cols_missing_values(missing_values_summary, 75)
df = drop_cols(df, cols_to_drop)
missing_values_rem = missing_values_table_info(df)
cols_to_imp = cols_to_impute(missing_values_rem)
to_impute, to_remove = filter_by_dtypes(df, cols_to_imp)
df = imput(df, to_impute)
df = clean_df_rows_missing_values(df)
save_csv(df, file_name)

