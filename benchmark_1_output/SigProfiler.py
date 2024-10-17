from SigProfilerAssignment import Analyzer as Analyze

samples = 'data/tumorBRCA.txt'

Analyze.cosmic_fit(samples, 'output', input_type="matrix", exome=False,
                   signature_database='data/COSMIC_v3.4_SBS_GRCh37.txt')