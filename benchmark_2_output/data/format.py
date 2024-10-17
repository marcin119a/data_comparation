import pandas as pd

# Wczytaj dane
df = pd.read_csv('counts_119breast.csv', index_col=0).reset_index()
df1 = pd.read_csv('breast_signatures.csv', sep='\t')

# Połączenie danych - dodanie pierwszej kolumny z df1
final_df = pd.concat([df1[['Type']].reset_index(drop=True), df], axis=1)

# Zapis do pliku
final_df.drop(columns='index').to_csv('counts.final.csv', sep='\t', index=False)