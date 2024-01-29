library(signature.tools.lib)

signatures_breast <- getOrganSignatures("Breast", typemut = "subs")


write.table(signatures_breast, "breast_signatures.csv", sep = "\t", row.names = TRUE, col.names = TRUE, quote = FALSE)