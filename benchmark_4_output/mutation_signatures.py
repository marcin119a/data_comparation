import numpy as np 

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
    tumorBRCA = np.genfromtxt('output/benchmark_3/data_for_deconstructSigs.dat', delimiter='\t', skip_header=1)
    tumorBRCA = np.delete(tumorBRCA, 0, axis=1)

    signaturesCOSMIC = np.genfromtxt('output/benchmark_3/COSMIC_V3_SBS.txt', delimiter='\t', skip_header=1)
    signaturesCOSMIC = np.delete(signaturesCOSMIC, 0, axis=1)
    df = pd.read_csv('output/benchmark_3/signatures_in_sample.csv')
    ground_truth = df.drop(columns=['Sample Names'])
    ground_truth.columns = [x for x in range(0, ground_truth.shape[1])]

    result_df, experiment_df = pd.DataFrame(), pd.DataFrame()

    for i in range(tumorBRCA.shape[1]):
        first_col = tumorBRCA[:, i]
        patient = ground_truth.iloc[i]
        patient = patient / patient.sum()

        non_zero_condition = (patient != 0)
        indexes = non_zero_condition[non_zero_condition].index.tolist()
        try:
            best_columns, b, estimation_exposures = backward_elimination(first_col, signaturesCOSMIC, threshold=0.01, mutation_count=None, R=25, significance_level=0.01)
        except:
            continue
        r = save_to_dataframe(indexes, patient[indexes].to_numpy(), df.iloc[i]['Sample Names'], 'Head-SCC')
        experiment_df = pd.concat([r, experiment_df], ignore_index=True)

        r = save_to_dataframe(best_columns, estimation_exposures[0], df.iloc[i]['Sample Names'], 'Head-SCC')
        result_df = pd.concat([r, result_df], ignore_index=True)


    experiment_df.to_csv('output/benchmark_3/ground_truth.csv')
    result_df.to_csv('output/benchmark_3/experiment.csv')