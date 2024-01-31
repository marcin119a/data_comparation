import pandas as pd

# Load the CSV files
wgs_signatures_df = pd.read_csv('M2.csv', sep=',')

# Transpose the WGS signatures dataframe
wgs_signatures_transposed = wgs_signatures_df.transpose()

# Rename the first row as the header and drop the index row
wgs_signatures_transposed.columns = wgs_signatures_transposed.iloc[0]
wgs_signatures_transposed = wgs_signatures_transposed.drop(wgs_signatures_transposed.index[0])

# Reset index to make the signatures as a column
wgs_signatures_transposed.reset_index(inplace=True)
wgs_signatures_transposed.rename(columns={'index': 'Patients'}, inplace=True)

# Display the first few rows of the transposed dataframe
wgs_signatures_transposed.head()
# Prepare the filename for the transposed WGS signatures dataframe
transposed_wgs_filename = 'M2.dec.csv'

# Save the transposed WGS signatures dataframe to CSV
wgs_signatures_transposed.to_csv(transposed_wgs_filename, index=False)


