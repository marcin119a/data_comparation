library(signature.tools.lib)
signature <- getOrganSignatures('Breast')
signatures2 <- read.csv("data/WGS_signatures__sigProfiler_SBS_signatures_2019_05_22.modified.csv")
row.names(signatures2) <- signatures2[,1]
signatures2 <- signatures2[,-1]

Fit(matrix, signatures2)
