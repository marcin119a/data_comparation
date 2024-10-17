
library(signature.tools.lib)
signatures <- read.csv("/home/mw/PycharmProjects/data_comparation/benchmark_1_output/data/COSMIC_v3.4_SBS_GRCh37.txt", sep='\t')
row.names(signatures) <- signatures[, 1]
signatures <- signatures[, -1]

catalogues <- read.csv("/home/mw/PycharmProjects/data_comparation/benchmark_1_output/data/tumorBRCA.txt", sep='\t')
row.names(catalogues) <- catalogues[, 1]
catalogues <- catalogues[,-1]

fit_results <- Fit(catalogues, signatures, method='NNLS')
save(fit_results, file = "/home/amso/Documents/data_comparation/data/fit_results.RData")

