
import pandas as pd

class DataFrameInfo:

    def __init__(self, df):
        self.df = df

    def display_head_tail(self):
        print("Head:")
        print(self.df.head())
        print("Tail:")
        print(self.df.tail())

    def display_shape(self):
        print("Shape:")
        print(self.df.shape)

    def display_info(self):
        print("Info:")
        print(self.df.info())

    def display_describe(self):
        print("Describe:")
        print(self.df.describe())

    def display_missing_values(self):
        print("Missing Values:")
        print(self.df.isnull().sum())

    def display_unique_values(self):
        print("Unique Values:")
        for column in self.df.columns:
            value_counts = self.df[column].value_counts()
            print(f"Column: {column}")
            print(value_counts)
            



class DataTransform:
    def __init__(self, df):
        self.df = df.copy()  

    def transform_date_columns(self, date_columns):
        for column in date_columns:
            self.df[column] = pd.to_datetime(self.df[column], format='%b-%y')

    def transform_categorical_columns(self, categorical_columns):
        self.df[categorical_columns] = self.df[categorical_columns].astype('category')

    def transform_boolean_column(self, boolean_column):
        self.df[boolean_column] = self.df[boolean_column].astype(bool)

    def transform_all_columns(self):
        date_columns = ['issue_date', 'earliest_credit_line', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date']
        categorical_columns = ['verification_status', 'loan_status', 'grade', 'term', 'sub_grade', 'purpose', 'home_ownership', 'collections_12_mths_ex_med', 'employment_length']
        boolean_column = 'payment_plan'

        self.transform_date_columns(date_columns)
        self.transform_categorical_columns(categorical_columns)
        self.transform_boolean_column(boolean_column)

        return self.df

