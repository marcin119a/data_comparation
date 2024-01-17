library(deconstructSigs)

tumor <- t(read.csv('/home/amso/Documents/data_comparation/data/M.csv', sep='\t'))
tumor <- as.data.frame(tumor)
tumor <- tumor[-1,]



signatures <- t(read.csv('/home/amso/Documents/data_comparation/data/WGS_signatures__sigProfiler_SBS_signatures_2019_05_22.modified.csv', sep='\t'))
signatures <- as.data.frame(signatures)
signatures <- signatures[-1,]

test = whichSignatures(tumor.ref = tumor, 
                       signatures.ref = signatures, sample.id = 1, 
                       contexts.needed = TRUE,
                       tri.counts.method = 'default')

t <- (randomly.generated.tumors)