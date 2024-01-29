
library(signature.tools.lib)
signatures <- read.csv("/home/amso/Documents/data_comparation/data/WGS_signatures__sigProfiler_SBS_signatures_2019_05_22.modified.csv", sep='\t')
row.names(signatures) <- signatures[, 1]
signatures <- signatures[, -1]

catalogues <- read.csv("/home/amso/Documents/data_comparation/data/M.csv", sep='\t')
row.names(catalogues) <- catalogues[, 1]
catalogues <- catalogues[,-1]

fit_results <- Fit(catalogues, signatures, method='NNLS')
save(fit_results, file = "/home/amso/Documents/data_comparation/data/fit_results.RData")