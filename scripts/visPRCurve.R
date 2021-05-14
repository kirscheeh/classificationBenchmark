#!/usr/bin/env Rscript
# this script visualizes the precision recall curve and return the area under the curve
# called from PRCurve.sh
args <- commandArgs(trailingOnly=TRUE)
print(args)
setwd(args[1]) #/mnt/fass1/kirsten/result/
require(PRROC)

# extract data sheet
sample.data <- read.csv(args[2], sep="\t")

# name for plot
sample.name.splitted <- strsplit(args[4], "/")
sample.name.vector <- sample.name.splitted[[1]]
sample.name <- sample.name.vector[length(sample.name.vector)]

groundTruth <- sample.data[,1]
abundances <- sample.data[,2]

fg <- abundances[groundTruth == 1]
bg <- abundances[groundTruth == 0]

# for saving as png
jpeg(file=args[3], width=850, height=632)

pr <- pr.curve(scores.class0 = fg, scores.class1 = bg, curve = T)
plot(pr, main=sample.name, col="black", panel.first= grid(), cex.main = 2);
print(sample.name)
print(pr)

baseline <- sum(groundTruth)/length(groundTruth)
abline(h=baseline, col="black", cex.main = 1, lty=2)


dev.off()



