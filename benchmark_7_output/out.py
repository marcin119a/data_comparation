import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../mutation_signatures')))
from model_selection_cv import backward_elimination

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
def main_block():
    tumor = np.genfromtxt('data/data_for_deconstructSigs.csv', delimiter='\t', skip_header=1)
    tumor = np.delete(tumor, 0, axis=1)

    result_df = pd.DataFrame()

    signaturesCOSMIC = np.genfromtxt('data/COSMIC_V3_SBS.txt', delimiter='\t', skip_header=1)
    signaturesCOSMIC = np.delete(signaturesCOSMIC, 0, axis=1)

    for i in range(tumor.shape[1]):
        first_col = tumor[:, i]
        try:
            best_columns, b, estimation_exposures = backward_elimination(first_col, signaturesCOSMIC, fold_size=4, threshold=0.01, significance_level=0.01)
            print(best_columns)
        except ValueError as e:
            print(e)
            continue
        r = save_to_dataframe(best_columns, estimation_exposures[0], f'{i}', '')

        result_df = pd.concat([r, result_df], ignore_index=True)
        result_df.to_csv('output/experiment.csv')


if __name__ == '__main__':
    main_block()