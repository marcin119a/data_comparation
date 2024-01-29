from SigProfilerAssignment import Analyzer as Analyze

samples = 'data/counts.final.csv'

Analyze.cosmic_fit(samples, 'output', input_type="matrix", exome=False,
                   signature_database='data/breast_signatures.csv')