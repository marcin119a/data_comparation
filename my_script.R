setwd('/home/amso/Documents/signature.tools.lib')

devtools::create("signature.tools.lib")

devtools::install()

library(signature.tools.lib)
signature <- getOrganSignatures('Breast')
signatures2 <- read.csv("/home/amso/data_comparation/pythonProject/data/WGS_signatures__sigProfiler_SBS_signatures_2019_05_22.modified.csv")
row.names(signatures2) <- signatures2[,1]
signatures2 <- signatures2[,-1]

catalogues <- read.csv("/home/amso/data_comparation/pythonProject/data/M1.csv")
catalogues <- catalogues[,-1]


Fit(catalogues, signatures2)

#if (!require("BiocManager", quietly = TRUE))
#    install.packages("BiocManager")

#BiocManager::install("BSgenome.Hsapiens.1000genomes.hs37d5")