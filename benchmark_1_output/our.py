from sigconfide.modelselection.analyzer import fit

fit('data/tumorBRCA.txt', 'output', signatures='data/COSMIC_v3.4_SBS_GRCh37.txt', threshold=0.01, mutation_count=1000, drop_zeros_columns=True)
