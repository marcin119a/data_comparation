from SigProfilerAssignment import Analyzer as Analyze

samples = 'data/data_for_deconstructSigs.csv'
#pip install SigProfilerAssignment
Analyze.cosmic_fit(samples, 'output', input_type="matrix", exome=False,
                   signature_database='data/COSMIC_V3_SBS.txt')