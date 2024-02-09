
library(signature.tools.lib)
signatures <- read.csv("/home/amso/Documents/data_comparation/benchmark_3_output/data/COSMIC_V3_SBS.txt", sep='\t')
row.names(signatures) <- signatures[, 1]
signatures <- signatures[, -1]

catalogues <- read.csv("/home/amso/Documents/data_comparation/benchmark_3_output/data/data_for_deconstructSigs.dat", sep='\t')
row.names(catalogues) <- catalogues[, 1]
catalogues <- catalogues[,-1]

fit_results <- Fit(catalogues, signatures, method='NNLS')
save(fit_results, file = "/home/amso/Documents/data_comparation/benchmark_3_output/output/fit_results.RData")

write.csv(values, file = "/home/amso/Documents/data_comparation/benchmark_3_output/output/signal.exposures.csv", row.names = FALSE)