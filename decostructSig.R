library(deconstructSigs)
library(reshape)

raw.my.signatures <- read.csv(
  "/home/amso/Documents/data_comparation/benchmark_1_output/data/all_signatures.csv",
  check.names = F)
my.signatures <- subset(raw.my.signatures, select=colnames(signatures.cosmic))
print(colnames(signatures.cosmic))
print(colnames(my.signatures))
rownames(my.signatures) <- make.names(rownames(my.signatures))
print(my.signatures)

raw.input <- read.csv(
  "/home/amso/Documents/data_comparation/benchmark_1_output/data/M2.dec.csv",
  check.names = F)
rownames(raw.input) <- raw.input$Patients
raw.input$Patients <- NULL

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
write.csv(final, '/home/amso/Documents/data_comparation/benchmark_1_output/deconstructsigs_output.csv')