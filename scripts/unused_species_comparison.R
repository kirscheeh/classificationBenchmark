# script for comparison
truth=c(0.1932, 0.1456, 0.1224, 0.1128, 0.0999, 0.0993, 0.097, 0.0928, 0.0192, 0.0178)#c(0.12,0.12,0.12,0.12,0.12,0.12,0.12,0.12,0.02,0.02)
kaiju.364 = c(0.008112241829185511, 0.09322046520153864, 0.10269090534142562, 0.04151326549024887, 0.017789189978776362, 0.02124483371952145, 0.011038583486806114, 0.1250292863300863, 0, 0)
ccmetagen.364 = c(0.00357422115547103, 0.11325804335808948, 0.017949584549420146, 0.09837457287785094, 0, 0.020692618126304997, 0.03386645433480648, 0, 0.008941424475638643, 1.145675504598455e-06)
centrifuge.364 = c(0.18033222980001143, 0.13268354876744617, 0.10978380289037058, 0.11039120082853578, 0.05890522708106204, 0.05824580663430398, 0.05114965525948968, 0.14248487058908882, 0, 0)
kraken2.364 = c(0.17514371067110807, 0.128698598552439, 0.11110932894921507, 0.11066767104219237, 0.05685214198356529, 0.05254612059953199, 0.04480679614709328, 0.14142218428763328, 0.021756091413448513, 0.020032995454532434)
diamond.364 = c(0.003931099075153449, 0.028948069393565312, 0.010118319637737405, 0.003972916231071292, 0.0025789155608511223, 0.0011511174632452977, 0.0010376955882900507, 0, 0, 0)
clark.364= c(0.07331721749790199, 0.13241545630823254, 0.11445298290938566, 0.11208258029037145, 0.05648781717310298, 0.04960860860574155, 0.04561564305333979, 0, 0, 0)
species=c('Bacillus subtilis', 'Listeria monocytogenes', 'Enterococcus faecalis', 'Staphylococcus aureus', 'Salmonella enterica', 'Escherichia coli', 'Pseudomonas aeruginosa', 'Lactobacillus fermentum', 'Saccharomyces cerevisiae', 'Cryptococcus neoformans')
length(species)
table.364 <- matrix(c(truth, c(ccmetagen.364, c(centrifuge.364, c(kraken2.364, c(clark.364, c(kaiju.364, diamond.364)))))), byrow = FALSE, nrow=10)
table.364.t <- t(table.364)

rownames(table.364.t) <- c("truth",  "ccmetagen", "centrifuge", "kraken2", "clark", "kaiju","diamond")
colnames(table.364.t) <- species

install.packages("ggplot2")
library(ggplot2)
ggplot(df_long, aes(x = DISTRICT, y = value, fill = variable)) + 
  geom_bar(stat = "identity", position = "dodge")

Species <- c(rep('Bacillus subtilis', 7), rep('Listeria monocytogenes', 7), rep('Enterococcus faecalis', 7), rep('Staphylococcus aureus', 7), rep('Salmonella enterica', 7), rep('Escherichia coli', 7), rep('Pseudomonas aeruginosa', 7),rep('Lactobacillus fermentum', 7), rep('Saccharomyces cerevisiae', 7), rep('Cryptococcus neoformans', 7))
length(species)
Tool <- rep(c("truth",  "ccmetagen", "centrifuge", "kraken2", "clark", "kaiju","diamond"),10)
Abundance.364 <- c(table.364.t[,1], c(table.364.t[,2], c(table.364.t[,3], c(table.364.t[,4], c(table.364.t[,5], c(table.364.t[,6], c(table.364.t[,7], c(table.364.t[,8], c(table.364.t[,9], table.364.t[,10])))))))))#c(truth, c(ccmetagen.364, c(centrifuge.364, c(kraken2.364, c(clark.364, c(kaiju.364, diamond.364))))))
data <- data.frame(Species,Tool.364,Abundance.364)       
p <- ggplot(data, aes(fill=Tool, y=Abundance.364, x=Species, label=Abundance.364)) + 
  geom_bar(position="dodge", stat="identity") 
  #geom_hline(yintercept = 0.12)
#+  geom_text(aes(label=Abundance), position=position_dodge(width=0.9), vjust=-0.25)
p + theme(axis.text.x = element_text(angle=-30, hjust=0)) + labs(y="Abundance", x="Species", title="Abundance of Species, gridion364")


kaiju.366 <- c(0.00049489, 0.57905155, 0.00010442999999999999, 4.008e-05, 0.00015487, 0.00018487, 0.009706939999999999, 4.308e-05, 0, 0)
centrifuge.366 <- c(0.01072083365219725, 0.8359701133790269, 0.00033009152023178085, 7.92219648556274e-05, 0.0005451225676970552, 0.0006041348476405327, 0.04598754221129522, 5.173679337510361e-05, 0, 0)
kraken2.366 <- c(0.010274629991165596, 0.8129274051937571, 0.0016234580693009913, 3.790068384831001e-05, 0.00048289288557810814, 0.0004796208840948008, 0.03980280737727268, 5.1534023362090594e-05, 0.006906649797681241, 2.699401223728555e-05)
ccmetagen.366 <- c(0.0002432328523018633, 0.7619671580435244, 0, 0, 0, 8.718023379995101e-07, 0.030071659246175768, 0, 0.0020060171797368727, 0)

table.366 <- matrix(c(ccmetagen.366, c(centrifuge.366, c(kraken2.366, kaiju.364))), byrow = FALSE, nrow=10)
table.366.t <- t(table.366)
species=c('Bacillus subtilis', 'Listeria monocytogenes', 'Enterococcus faecalis', 'Staphylococcus aureus', 'Salmonella enterica', 'Escherichia coli', 'Pseudomonas aeruginosa', 'Lactobacillus fermentum', 'Saccharomyces cerevisiae', 'Cryptococcus neoformans')

rownames(table.366.t) <- c("ccmetagen", "centrifuge", "kraken2", "kaiju")
colnames(table.366.t) <- species

Species <- c(rep('Bacillus subtilis', 4), rep('Listeria monocytogenes', 4), rep('Enterococcus faecalis', 4), rep('Staphylococcus aureus', 4), rep('Salmonella enterica', 4), rep('Escherichia coli', 4), rep('Pseudomonas aeruginosa', 4),rep('Lactobacillus fermentum', 4), rep('Saccharomyces cerevisiae', 4), rep('Cryptococcus neoformans', 4))
length(Species)
Tool <- rep(c("ccmetagen", "centrifuge", "kraken2", "kaiju"),10)
length(Tool)
Abundance.366 <- c(table.366.t[,1], c(table.366.t[,2], c(table.366.t[,3], c(table.366.t[,4], c(table.366.t[,5], c(table.366.t[,6], c(table.366.t[,7], c(table.366.t[,8], c(table.366.t[,9], table.366.t[,10])))))))))#c(truth, c(ccmetagen.364, c(centrifuge.364, c(kraken2.364, c(clark.364, c(kaiju.364, diamond.364))))))
data <- data.frame(Species,Tool,Abundance.366)       
p <- ggplot(data, aes(fill=Tool, y=Abundance.366, x=Species, label=Abundance.366)) + 
  geom_bar(position="dodge", stat="identity") +
  geom_hline(yintercept = 0.891)
#+  geom_text(aes(label=Abundance), position=position_dodge(width=0.9), vjust=-0.25)
p + theme(axis.text.x = element_text(angle=-30, hjust=0)) + labs(y="Abundance", x="Species", title="Abundance of Species, gridion366")





