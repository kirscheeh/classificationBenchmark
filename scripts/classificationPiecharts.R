#!/usr/bin/env Rscript
# piecharts based on the areports 

install.packages("ggrepel")

args <- commandArgs(trailingOnly=TRUE)
report <- read.csv(args[1], sep="\t")
name <- "/home/kirscheeh/university/projectCLASSIFICATION/classificationBenchmark/areports/gridion364_default.diamond.areport"
report <- read.csv(name, sep="\t")
sample.name.splitted <- strsplit(name, "/")
sample.name.vector <- sample.name.splitted[[1]]
sample.name <- sample.name.vector[length(sample.name.vector)]

abundances <- report[,c(1, 3,5)]
sum(abundances[,1])

# getting species with at least 1% abundance
species <- c()
for (i in 1:length(report[,1])){
  if (abundances[i, 1] >= 0.01 && ("G" ==abundances[i, 2] || grepl("U", abundances[i, 2])))
  {
    species <- c(species, abundances[i,1], as.character(abundances[i, 2]), as.character(abundances[i, 3]))
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
save <- "/home/kirscheeh/university/projectCLASSIFICATION/classificationBenchmark/stats/pics/gridion364_default.diamond.genus.piechart.jpeg"
#jpeg(filename=save, width=850, height=632)
library(ggplot2)
df <- data.frame(value=species.slices, group=labels)
#pie(species.slices,labels,main=sample.name, cex=1)
df <- data.frame(
  group=LETTERS[1:5],
  value=c(13,7,9,21,2)
)
ggplot(df, aes(x="", y=value, fill=group))+
geom_bar(stat="identity", width=1, color="white") +
  coord_polar("y", start=0) +
  theme_void() # remove background, grid, numeric labels
install.packages("dplyr")
library(dplyr)
library(ggrepel)
set.seed(42)
data <- df %>% 
  arrange(desc(group)) %>%
  mutate(prop = value / sum(data$value) *100) %>%
  mutate(ypos = cumsum(prop)- 0.5*prop )

# Basic piechart
ggplot(data, aes(x="", y=prop, fill=group)) +
  geom_bar(stat="identity", width=1, color="white", cex=0.5) +
  coord_polar("y", start=0) +
  theme_void() + 
  theme(legend.position="none") +
  geom_text(aes(y = ypos, label = group), nudge_x=0.5, nudge_y=0.25,color = "black", size=3) +
  scale_fill_brewer(palette="Set1")


#dev.off()


# Load ggplot2
library(ggplot2)

# Create Data
data <- data.frame(
  group=LETTERS[1:5],
  value=c(13,7,9,21,2)
)

# Basic piechart
ggplot(data, aes(x="", y=value, fill=group)) +
  geom_bar(stat="identity", width=1) +
  coord_polar("y", start=0)


