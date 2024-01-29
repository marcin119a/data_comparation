import pandas as pd


df = pd.read_csv('benchmark_1_output/data_syntetic/WGS_signatures__sigProfiler_SBS_signatures_2019_05_22.csv')
df = df.drop(columns=['SubType', 'Type'])

#todo replace
#df['Type'].replace("C>A,", "[C>A]")


df.to_csv('data/WGS_signatures__sigProfiler_SBS_signatures_2019_05_22.modified.csv',index=True )