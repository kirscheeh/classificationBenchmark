#!/usr/bin/env Rscript
# piecharts based on the areports 

args <- commandArgs(trailingOnly=TRUE)
report <- read.csv(args[1], sep="\t")
name <- "/home/kirscheeh/university/projectCLASSIFICATION/classificationBenchmark/areports/gridion366_default.diamond.areport"
report <- read.csv(name, sep="\t")
sample.name.splitted <- strsplit(name, "/")
sample.name.vector <- sample.name.splitted[[1]]
sample.name <- "gridion364_custom.diamond.areport - Genus" # sample.name.vector[length(sample.name.vector)]

abundances <- report[,c(1, 3,5)]
sum(abundances[,1])

# getting species with at least 1% abundance
species <- c()
for (i in 1:length(report[,1])){
  if (abundances[i, 1] >= 0.01 && ("S" == abundances[i, 2] || grepl("U", abundances[i, 2])))
  {
    if (abundances[i, 3] == "Limosilactobacillus fermentum") {
      species <- c(species, abundances[i,1], as.character(abundances[i, 2]), as.character("Lactobacillus fermentum"))
    }
    else{
      species <- c(species, abundances[i,1], as.character(abundances[i, 2]), as.character(abundances[i, 3]))
      
    }
  }}

species.matrix <- matrix(species, ncol=3, byrow=TRUE)

# preparing slices
species.slices <- as.numeric(species.matrix[,1])
sum(species.slices)
underOnePercent <- 1-sum(species.slices)
species.slices <- c(species.slices, underOnePercent)

# preparing labels
labels <- species.matrix[, 3]
labels <- c(labels, "others")
species.percent <- round(species.slices/sum(species.slices)*100, 3)
labels <- paste(labels, species.percent) # add percentages to labels
labels <- paste(labels,"%",sep="") # add % to labels

save <- "/home/kirscheeh/university/projectCLASSIFICATION/classificationBenchmark/stats/pics/gridion364_custom.diamond.genus.piechart.jpeg"
jpeg(filename=save, width=850, height=632)
pie(species.slices,labels,main=sample.name, cex=1)
dev.off()
