#!/usr/bin/env Rscript
# UNEXECUTED TEMPLATE. R/edgeR unavailable in package-build environment.
# Input: raw integer pseudobulk counts, genes x samples, row names in first column.
# Metadata CSV: sample_id, donor_id, condition. One cell population per invocation.
# Usage: Rscript pseudobulk_edger.R counts.csv metadata.csv control case unpaired output.csv
# For complete within-donor pairing use paired; extra batches require a reviewed design.
args <- commandArgs(trailingOnly=TRUE)
if (length(args)!=6) stop('Expected: counts.csv metadata.csv reference test paired|unpaired output.csv')
if (!requireNamespace('edgeR',quietly=TRUE)) stop('Install an explicit reviewed edgeR version in a dedicated environment')
counts <- as.matrix(read.csv(args[1],row.names=1,check.names=FALSE))
meta <- read.csv(args[2],stringsAsFactors=FALSE,check.names=FALSE)
if (!all(c('sample_id','donor_id','condition') %in% names(meta))) stop('Missing metadata columns')
if (anyDuplicated(meta$sample_id) || anyDuplicated(colnames(counts))) stop('Duplicate sample identifiers')
if (anyNA(meta[,c('sample_id','donor_id','condition')])) stop('Missing metadata values')
if (!setequal(meta$sample_id,colnames(counts))) stop('Sample IDs mismatch')
meta <- meta[match(colnames(counts),meta$sample_id),,drop=FALSE]
if (!is.numeric(counts) || any(!is.finite(counts)) || any(counts<0) || any(abs(counts-round(counts))>1e-8))
  stop('Counts must be finite nonnegative integers, not normalized or imputed expression')
if (any(colSums(counts)<=0)) stop('Empty pseudobulk; absent populations are not zero-expression replicates')
if (args[3]==args[4] || !setequal(unique(meta$condition),c(args[3],args[4]))) stop('Exactly two specified conditions required')
meta$condition <- factor(meta$condition,levels=c(args[3],args[4]))
meta$donor_id <- factor(meta$donor_id)
mode <- args[5]
if (mode=='paired') {
  if (!all(table(meta$donor_id,meta$condition)==1)) stop('Template requires exactly one pseudobulk per donor per condition')
  design <- model.matrix(~ donor_id + condition,data=meta)
} else if (mode=='unpaired') {
  if (anyDuplicated(meta$donor_id)) stop('Repeated donor rows require aggregation or a justified repeated-measures model')
  design <- model.matrix(~ condition,data=meta)
} else stop('Mode must be paired or unpaired')
if (qr(design)$rank != ncol(design)) stop('Rank-deficient design')
if (nrow(design)<=ncol(design)) stop('No residual degrees of freedom')
y <- edgeR::DGEList(counts=counts)
keep <- edgeR::filterByExpr(y,design=design)
if (!any(keep)) stop('No genes pass expression filtering')
y <- y[keep,,keep.lib.sizes=FALSE]
y <- edgeR::calcNormFactors(y)
y <- edgeR::estimateDisp(y,design)
fit <- edgeR::glmQLFit(y,design)
contrast_col <- grep('^condition',colnames(design))
if (length(contrast_col)!=1) stop('Ambiguous contrast; review design')
ql <- edgeR::glmQLFTest(fit,coef=contrast_col)
res <- edgeR::topTags(ql,n=Inf,sort.by='none')$table
# Family here = tested genes for THIS population/contrast only.
# Several populations/contrasts require preplanned joint/hierarchical correction.
res$FDR_within_population_contrast <- p.adjust(res$PValue,method='BH')
res$gene_id <- rownames(res)
write.csv(res,args[6],row.names=FALSE)
capture.output(sessionInfo(),file=paste0(args[6],'.session.txt'))
write.csv(design,paste0(args[6],'.design.csv'))
message('Template execution does not validate label selection, patient sampling, or causal interpretation.')
