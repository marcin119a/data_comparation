
library(signature.tools.lib)
signatures <- read.csv("/home/amso/Documents/data_comparation/data/WGS_signatures__sigProfiler_SBS_signatures_2019_05_22.modified.csv")
row.names(signatures) <- signatures[,1]
signatures <- signatures[,-1]

catalogues <- read.csv("/home/amso/Documents/data_comparation/data/M.csv", sep='\t')
catalogues <- catalogues[,-1]
row.names(catalogues) <- catalogues[,1]

fit_results <- Fit(catalogues, signatures2)


#if (!require("BiocManager", quietly = TRUE))
#    install.packages("BiocManager")

#BiocManager::install("BSgenome.Hsapiens.1000genomes.hs37d5")