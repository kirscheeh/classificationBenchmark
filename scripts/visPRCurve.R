#!/usr/bin/env Rscript
# this script visualizes the precision recall curve and return the area under the curve

#check if required packages is installes
#list.packages <- c("PRROC")
#print(list.packages)
#packages.new <- list.packages[!(list.packages %in% installed.packages()[,"Package"])]
#print(packages.new)
#if (length(packages.new)>0) { 
#    install.packages("PRROC", lib="/home/re85gih/miniconda3/envs/projectMAIN/lib/R/library")
#}
setwd("/home/kirscheeh/university/projectCLASSIFICATION/classificationBenchmark/scripts") #/mnt/fass1/kirsten/result/
require(PRROC)

# extract data sheet
args <- commandArgs(trailingOnly=TRUE)
#file <- "/home/kirscheeh/university/projectCLASSIFICATION/classificationBenchmark/helper.tsv"
sample.data <- read.csv(args[1], sep="\t") #args[1]

# name for plot
sample.name.splitted <- strsplit(args[3], "/")
sample.name.vector <- sample.name.splitted[[1]]
sample.name <- sample.name.vector[length(sample.name.vector)]

groundTruth <- sample.data[,1]
abundances <- sample.data[,2]

fg <- abundances[groundTruth == 1]
bg <- abundances[groundTruth == 0]

# for saving as png
jpeg(file=args[2], width=850, height=632)

pr <- pr.curve(scores.class0 = fg, scores.class1 = bg, curve = T)
plot(pr, main=sample.name, col="black", panel.first= grid(), cex.main = 2);
print(sample.name)
print(pr)

baseline <- sum(groundTruth)/length(groundTruth)
abline(h=baseline, col="black", cex.main = 1, lty=2)
#print(baseline)

dev.off()

#x <- c(fg, bg)
#lab<- c(rep(1,length(fg)),rep(0,length(bg)))
#pr <- pr.curve(scores.class0 = x, weights.class0 = lab, curve=T)
#plot(pr, main=sample.name, col="black", panel.first= grid(), cex.main = 2);
