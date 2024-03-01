from SigProfilerAssignment import Analyzer as Analyze

samples = 'data/M1.csv'

Analyze.t (samples, 'output', input_type="matrix", exome=False,
                   signature_database='data/WGS_signatures__sigProfiler_SBS_signatures_2019_05_22.modified.csv')