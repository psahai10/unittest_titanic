import pandas as pd
import numpy as np
import os.path 


@pytest.fixture()
def get_df(file_path):
    df = pd.read_csv(file_path)
    return df

def missing_values(df):
    df_is_null = df.isnull()
    return sum_of_missing_values

def perc_missing_values(df):
    # Percentage of missing values
    return 100 * df.isnull().sum() / len(df)

def columns_dtypes(df):
    # Coumn for dtypes
    return df.dtypes

def missing_values_table_info(df):
    mis_val = missing_values_info(df)
    mis_val_percent = perc_missing_values(df)
    dtype = columns_dtypes(df)
    mis_val_table = pd.concat([mis_val, mis_val_percent,dtype], axis=1)
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values', 2:'Data Types'})
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
    '% of Total Values', ascending=False).round(1)
    return mis_val_table_ren_columns

def clean_df_cols_missing_values(summary_df, threshold=75):
    return summary_df[summary_df["% of Total Values"] > threshold].index.tolist()

def drop_cols(df, cols):
    copy = df.copy()
    return copy.drop(columns=cols)

def clean_df_rows_missing_values(df):
    df1 = df.dropna()
    return df1

def cols_to_impute(df, _min=0, _max=25):
    min_cols_to_impute = df[df["% of Total Values"] >= _min].index.tolist()
    max_cols_to_impute = df[df["% of Total Values"] <= _max].index.tolist()
    return list(set(min_cols_to_impute ) and set(max_cols_to_impute))

def filter_by_dtypes(df, lst):
    nums, others = [], []
    dtypes_list = df[lst].dtypes.tolist() 
    for col, types in zip(lst, dtypes_list):
        if types in ['float', 'int']:
            nums.append(col)
        else:
            others.append(col)
    return nums, others

def imput(df, cols):
    if cols:
        for col in cols:
            value = df[col].mean()
            df[col].fillna(value, inplace=True)
    return df

file_name = '../data/clean/clean_train.csv'

def save_csv(df, file_name):
    # if os.path.isfile(file_name):
    #     pass
    # else:
    df.to_csv(file_name)

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

