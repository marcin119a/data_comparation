import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../mutation_signatures')))
from model_selection import backward_elimination
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
    tumor = np.genfromtxt('data/data_for_deconstructSigs.csv', delimiter='\t', skip_header=1)
    tumor = np.delete(tumor, 0, axis=1)

    signaturesCOSMIC = np.genfromtxt('data/COSMIC_V3_SBS.txt', delimiter='\t', skip_header=1)
    signaturesCOSMIC = np.delete(signaturesCOSMIC, 0, axis=1)
    df = pd.read_csv('data/signatures_in_sample.csv')
    ground_truth = df.drop(columns=['Sample Names', 'Cancer'])
    ground_truth.columns = [x for x in range(0, ground_truth.shape[1])]

    result_df, experiment_df = pd.DataFrame(), pd.DataFrame()
    print(tumor.shape[1])
    for i in range(tumor.shape[1]):
        first_col = tumor[:, i]
        patient = ground_truth.iloc[i]
        patient = patient / patient.sum()

        non_zero_condition = (patient != 0)
        indexes = non_zero_condition[non_zero_condition].index.tolist()
        try:
            best_columns, b, estimation_exposures = backward_elimination(first_col, signaturesCOSMIC, threshold=0.01, mutation_count=None, R=25, significance_level=0.01)
        except:
            continue
        r = save_to_dataframe(indexes, patient[indexes].to_numpy(), df.iloc[i]['Sample Names'],  df.iloc[i]['Cancer'])
        experiment_df = pd.concat([r, experiment_df], ignore_index=True)

        r = save_to_dataframe(best_columns, estimation_exposures[0], df.iloc[i]['Sample Names'], df.iloc[i]['Cancer'])
        result_df = pd.concat([r, result_df], ignore_index=True)
        print(best_columns)

        experiment_df.to_csv('output/ground_truth.csv')
        result_df.to_csv('output/experiment.csv')