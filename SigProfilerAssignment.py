from SigProfilerAssignment import Analyzer as Analyze

samples = 'data/count_syntetic2.csv'

Analyze.cosmic_fit(samples, 'benchmark_1_output', input_type="matrix", exome=False,
                   signature_database='data/WGS_signatures__sigProfiler_SBS_signatures_2019_05_22.modified.csv')