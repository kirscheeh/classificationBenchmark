#lines = readLines("/home/kirscheeh/Downloads/ERR3152364.fastq")
lines= c("axcgtacgtcgatcga", "cagctacgatcgatcgatcg", "acastcgatcazc", "aczascgasczgzasc")
seqLength <- c()
for (i in 1:length(lines)){
  if (i %% 4 == 2)
  {
    seqLength <- c(seqLength, nchar(lines[i]))
    print(i)
  }
}

png(filename="/home/kirscheeh/university/projectCLASSIFICATION/classificationBenchmark/stats/gridion364_readlength.png", width=850, height=632)

hist(seqLength, xaxt='n',yaxt='n', main="Distribution of read lengths for gridion364.fastq", breaks=1000, xlim=c(0, 20000), ylim=c(0, 30000), xlab="", ylab="", col="lightblue")
title(xlab="read length", line=4, cex.lab=1.2)
title(ylab="abundance", line=3.2, cex.lab=1.2)
axis(side=2, las=1, col="grey")
axis(side=1, at=c(0, 2000, 3370, 4000, 6000, 8000, 10000, 12000, 14000,16000,18000,20000,22000), las=3, col="grey")
axis(side=1, at=c(3370), las=3, col="grey")

median <- median(seqLength)
abline(v=median, col="darkmagenta", lwd=2)
text(15000, 30000, "Median: 3370")#14100
text(15000, 28000, 'Average: 4119')#14200
text(15000, 26000, 'Shortest Sequence: 3')#15100
text(15000, 24000, 'Longest Sequence: 267641')#16000

dev.off()
