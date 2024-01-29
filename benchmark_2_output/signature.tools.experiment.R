
library(signature.tools.lib)
signatures <- read.csv("/home/amso/Documents/data_comparation/benchmark_2_output/data/breast_signatures.csv", sep='\t')
row.names(signatures) <- signatures[, 1]
signatures <- signatures[, -1]

catalogues <- read.csv("/home/amso/Documents/data_comparation/benchmark_2_output/data/counts.csv", sep='\t')
row.names(catalogues) <- catalogues[, 1]
catalogues <- catalogues[,-1]

fit_results <- Fit(catalogues, signatures, method='NNLS')
save(fit_results, file = "/home/amso/Documents/data_comparation/benchmark_2_output/output/fit_results.RData")

