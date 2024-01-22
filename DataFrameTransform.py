import pandas as pd
import numpy as np

class DataFrameTransform:

    def __init__(self, df):
        self.df = df.copy()

    def drop_columns_with_many_nulls(self, threshold_fraction=0.5):
        threshold = int((1 - threshold_fraction) * len(self.df))
        self.df = self.df.dropna(axis=1, thresh=threshold)

    def impute_randomly(self, column_name):
        column = self.df[column_name]
        null_indices = column.isnull()
        num_nulls = null_indices.sum()
        if num_nulls > 0:
            non_null_values = column.dropna()
            random_values = np.random.choice(non_null_values, size=num_nulls)
            column.loc[null_indices] = random_values
            self.df[column_name] = column
        return self.df

    def impute_randomly_columns(self):
        columns_to_impute_randomly = ['term', 'employment_length', 'last_credit_pull_date', 'last_payment_date', 'collections_12_mths_ex_med']
        for column in columns_to_impute_randomly:
            self.df = self.impute_randomly(column)

    def impute_mean_columns(self):
        columns_to_impute_mean = ['int_rate', 'funded_amount']
        for column in columns_to_impute_mean:
            self.df[column].fillna(self.df[column].mean(), inplace=True)


numerical_columns = ['loan_amount', 'funded_amount', 'funded_amount_inv', 'int_rate', 'instalment', 'annual_inc', 'dti', 'delinq_2yrs', 'inq_last_6mths', 'open_accounts', 'total_accounts', 'out_prncp', 'out_prncp_inv', 'total_payment', 'total_payment_inv', 'total_rec_prncp', 'total_rec_int', 'total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 'last_payment_amount']
class DataFrameTransformSkewandOutliers:

    def __init__(self, df):
        self.df = df

    def identify_skewed_columns(self, skew_threshold=0.8):
        # Identify columns with skewness greater than the threshold
        skewness = self.df[numerical_columns].apply(lambda x: x.skew())
        skewed_columns = skewness[abs(skewness) > skew_threshold].index.tolist()
        return skewed_columns

    def transform_skewed_columns(self, columns=None, transformation='log'):
        # If columns are not specified, use all numeric columns
        if columns is None:
            columns = self.df.select_dtypes(include=['number']).columns.tolist()

        # Perform transformations on specified columns
        for column in columns:
            if transformation == 'log':
                self.df[column] = np.log1p(self.df[column])

    def remove_outliers_iqr(self, numerical_columns, multiplier=1.5):
        for column_name in numerical_columns:
            # Calculate Q1 and Q3
            Q1 = self.df[column_name].quantile(0.25)
            Q3 = self.df[column_name].quantile(0.75)

            # Calculate IQR
            IQR = Q3 - Q1
            lower_bound = Q1 - multiplier * IQR
            upper_bound = Q3 + multiplier * IQR

            # Filter out outliers
            self.df = self.df[(self.df[column_name] >= lower_bound) & (self.df[column_name] <= upper_bound)]

    def remove_highly_correlated_columns(self, highly_correlated_columns):
        # Remove highly correlated columns
        self.df = self.df.drop(columns=highly_correlated_columns)