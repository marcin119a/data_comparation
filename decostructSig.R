library(deconstructSigs)
library(reshape)

raw.my.signatures <- read.csv(
  "/home/amso/Documents/mutation_signatures/output/WGS_signatures__sigProfiler_SBS_signatures_2019_05_22.modified.csv",
  sep = '\t',
  check.names = F,
  row.names = 1)

raw.my.signatures <- t(raw.my.signatures)

raw.input <- read.csv(
  "/home/amso/Documents/mutation_signatures/output/M.csv",
  sep = '\t',
  check.names = F)

raw.input$`Unnamed: 0` <- NULL
raw.input <- t(raw.input)

result <- list()
for(sample in rownames(raw.input)) {
  print(sample)
  output <- whichSignatures(tumor.ref = raw.input,
                            sample.id = sample,
                            contexts.needed = TRUE,
                            signature.cutoff = 0.00,
                            tri.counts.method = "default",
                            signatures.ref = my.signatures)
  
  # makePie(output, sub=sample)
  output$weights['Sample'] <- sample
  result[[sample]] <- output$weights
}

final = reshape::merge_all(result)
write.csv(final, '~/sinai/git/paper-201604/data/derived/deconstructsigs_output.csv')