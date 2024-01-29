import pandas as pd

df = pd.read_csv('counts_119breast.csv', index_col=0).reset_index()


df1 = pd.read_csv('breast_signatures.csv', sep='\t')
#todo columns
pd.concat([df1[['Type']], df], axis=1, ignore_index=True).drop(columns=[1]).to_csv('counts.final.csv', sep='\t', index=False)
