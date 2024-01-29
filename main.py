import pandas as pd
import numpy as np

if __name__ == '__main__':
    df_exposures = pd.read_csv('data/data_syntetic/WGS-decomposition__PCAWG_sigProfiler_SBS_signatures_in_samples.csv')
    exposures = df_exposures[(df_exposures.columns[3:])].values
    df_signatures = pd.read_csv('data/data_syntetic/WGS_signatures__sigProfiler_SBS_signatures_2019_05_22.csv')
    signatures = df_signatures[(df_exposures.columns[3:])].values
    pd.DataFrame(signatures).to_csv('signatures.csv')

    M = np.dot(signatures, exposures.T)
    patients = 4
    df = pd.DataFrame(M.round().astype(int), index=df_signatures['SubType'].values)
    print(df_exposures['Sample Names'].values)
    df.to_csv('count_syntetic2.csv', header=df_exposures['Sample Names'].values)


