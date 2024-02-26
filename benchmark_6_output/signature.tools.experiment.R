
library(signature.tools.lib)
signatures <- read.csv("/home/amso/Documents/data_comparation/benchmark_6_output/data/COSMIC_V3_SBS.txt", sep='\t')
row.names(signatures) <- signatures[, 1]
signatures <- signatures[, -1]

catalogues <- read.csv("/home/amso/Documents/data_comparation/benchmark_6_output/data/data_for_deconstructSigs.csv", sep='\t')
#catalogues <- catalogues[,-1]

fit_results <- Fit(catalogues, signatures, method='KLD', useBootstrap = TRUE, nboot = 100,   nparallel = 4)
save(fit_results, file = "/home/amso/Documents/data_comparation/benchmark_6_output/output/fit_results.RData")
#todo boostrap
write.csv(fit_results$exposures, file = "/home/amso/Documents/data_comparation/benchmark_6_output/output/signal.exposures.csv", row.names = FALSE)