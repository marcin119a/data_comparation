import numpy as np
import os
import sys
def save_to_dataframe(best_columns, findSigExposures, cancer_type, patient):
    """
    Saves the best_columns and findSigExposures to a pandas DataFrame.
    """
    # Create a DataFrame with findSigExposures as a column
    df = pd.DataFrame(findSigExposures, columns=['findSigExposures'])
    # Add the best_columns as another column, ensuring the length matches
    # If best_columns is shorter, pad with None or a default value
    df['best_columns'] = pd.Series(best_columns).reindex(df.index)
    df['Cancer Types'] = cancer_type
    df['Sample Names'] = patient

    return df

#to test
import pandas as pd
if __name__ == '__main__':

    df = pd.read_csv('data/signatures_in_sample.csv')
    print(df.columns)
    ground_truth = df.drop(columns=['Sample Names', 'Cancer'])
    ground_truth.columns = [x for x in range(0, ground_truth.shape[1])]

    result_df, experiment_df = pd.DataFrame(), pd.DataFrame()
    print(ground_truth.shape[0])
    for i in range(ground_truth.shape[0]):
        patient = ground_truth.iloc[i]
        patient = patient / patient.sum()

        non_zero_condition = (patient != 0)
        indexes = non_zero_condition[non_zero_condition].index.tolist()
        r = save_to_dataframe(indexes, patient[indexes].to_numpy(), df.iloc[i]['Sample Names'], df.iloc[i]['Cancer'])
        experiment_df = pd.concat([r, experiment_df], ignore_index=True)


    experiment_df.to_csv('output/ground_truth.csv')
