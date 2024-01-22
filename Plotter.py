import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Plotter:

    def __init__(self, df):
        self.df = df

    def display_value_counts(self):
        for column in self.df.columns:
            value_counts = self.df[column].value_counts()
            print(f"Column: {column}")
            print(value_counts)

    def display_null_values(self):
        view_nulls_before = self.df.isnull().sum()
        view_percentage_nulls_before = self.df.isnull().sum() * 100 / len(self.df)

        print(view_nulls_before)
        print(view_percentage_nulls_before)

    def visualize_null_values_heatmap(self):
        plt.figure(figsize=(10, 6))
        sns.heatmap(self.df.isnull(), cbar=False, cmap='viridis')
        plt.title('Null Values Distribution')
        plt.show()

    def display_numeric_summary(self):
        print(self.df.describe)
    def visualize_skew(self):
        numerical_columns = ['loan_amount', 'funded_amount', 'funded_amount_inv', 'int_rate', 'instalment', 'annual_inc', 'dti', 'delinq_2yrs', 'inq_last_6mths', 'open_accounts', 'total_accounts', 'out_prncp', 'out_prncp_inv', 'total_payment', 'total_payment_inv', 'total_rec_prncp', 'total_rec_int', 'total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 'last_payment_amount']
        skewness = self.df[numerical_columns].skew()

        plt.figure(figsize=(8, 6))
        skewness.plot(kind='bar', color='skyblue')
        plt.title('Skewness of Numerical Columns')
        plt.xlabel('Columns')
        plt.ylabel('Skewness')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.show()

    def visualize_skew_sns(self):
        numeric_features = [col for col in self.df.columns if self.df[col].dtype in ['int64', 'float64']]
        sns.set(font_scale=0.7)
        f = pd.melt(self.df[numeric_features].reset_index(), id_vars="index", value_vars=numeric_features)
        g = sns.FacetGrid(f, col="variable", col_wrap=3, sharex=False, sharey=False)
        g = g.map(sns.histplot, "value", kde=True)
        plt.show()

    def visualize_outliers_boxplot(self):
        numerical_columns = ['loan_amount', 'funded_amount', 'funded_amount_inv', 'int_rate', 'instalment', 'annual_inc', 'dti', 'delinq_2yrs', 'inq_last_6mths', 'open_accounts', 'total_accounts', 'out_prncp', 'out_prncp_inv', 'total_payment', 'total_payment_inv', 'total_rec_prncp', 'total_rec_int', 'total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 'last_payment_amount']

        # Plot size
        fig, axes = plt.subplots(nrows=len(numerical_columns), figsize=(6, 4 * len(numerical_columns)))

        # Create a boxplot
        for i, column_name in enumerate(numerical_columns):
            sns.boxplot(x=self.df[column_name], ax=axes[i], color='green')
            axes[i].set_title(f'Boxplot for {column_name}')

        plt.tight_layout()
        plt.show()

    def visualize_correlation_matrix(self):
        numerical_columns = ['loan_amount', 'funded_amount', 'funded_amount_inv', 'int_rate', 'instalment', 'annual_inc', 'dti', 'delinq_2yrs', 'inq_last_6mths', 'open_accounts', 'total_accounts', 'out_prncp', 'out_prncp_inv', 'total_payment', 'total_payment_inv', 'total_rec_prncp', 'total_rec_int', 'total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 'last_payment_amount']
        correlation_matrix = self.df[numerical_columns].corr()

        plt.figure(figsize=(12, 10))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Matrix')
        plt.show()

    def identify_highly_correlated_variables(self, corr_threshold=0.90):
        numerical_columns = ['loan_amount', 'funded_amount', 'funded_amount_inv', 'int_rate', 'instalment', 'annual_inc', 'dti', 'delinq_2yrs', 'inq_last_6mths', 'open_accounts', 'total_accounts', 'out_prncp', 'out_prncp_inv', 'total_payment', 'total_payment_inv', 'total_rec_prncp', 'total_rec_int', 'total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 'last_payment_amount']
        correlation_matrix = self.df[numerical_columns].corr()
        upper = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1) == 1)
        highly_correlated_columns = [column for column in upper.columns if any(upper[column] > corr_threshold)]
        print("Highly Correlated Columns:", highly_correlated_columns)


