#
## Introduction
## Material and Methods
### Data
The present dataset consists of four samples of the underlying ZymoBIOMICS Microbial Community Standards CS and CSII (Quelle: Zymo-Website, DataPaper). Those mock communities are composed of ten microbial species, eight bacteria and two fungi (Table 1). Each of these two standards is sequenced with GridION and PromethION, resulting in four samples, two for each standard. 
[Hier Tabelle 1]
[Hier Tabelle 2]
The samples sequenced with PromethION show a higher read count with an average of 35.1 million reads and a median quality of 10.6. The GridION samples consist of approximately 3.5 million reads with a quality of 10 (Table 2, Quelle Data).
The ZymoBIOMICS Microbial Community Standards come with knowledge about the abundance of the different species, which differ for CS and CSII. In the following, CS will be referred to as CS Even, since the abundances are 12% for each bacterial species and 2% for the two fungi, whereas CSII abundances follow a log distribution and will be referred to as CS Log (Quelle: Zymo). The different abundances (expected and estimated) can be seen in Table 3 (Quelle Data, Zymo).
[Hier Tabelle 3]

### Tools
### Classification
#### Others
Additional to the classification tools, conda (Referenz) is used to organise and coordinate the different requirements of the tools. The tools themselves and their execution are structured with snakemake (Referenz). Some analysis is done with Python, R and Bash (Tabelle 4).
[Hier Tabelle 4]
### Metrics
## Results and Discussion
### Comparison using the metrics
#### Area under Preicison Recall Curve
#### Abundance Profile Similarity
#### Time
### Classification Results
The following section shows the species in the diagrams that had an abundance of at least one per cent. Reads that were not assigned to a species but other taxa, or are below the 1% mark, are summarized in "Others".
#### Diamond
As mentioned earlier **[Tabelle X]**, Diamond can classify 84.23% and [PromethionEven Hier], respectively, for the CS Even samples (gridion364, promethion365, Link zu areports) with the default database. However, in the sample sequenced with GridION, Diamond is only able to identify Limosilactobacillus fermentum with 4.812% abundance, Enterococcus faecalis with 1.012% and Listeria monocytogenes with 2.895% on species level. Over 75% of the reads couldn’t be assigned to a species. For PromethION, the results are [similar, different, whatever]. therefore, Diamond is not able to classify the majority of the species in the sample, with many species having low abundances **[Tabelle X]**. This does [not] change for a greater sequencing depth.
|||
|:--|:--|
|![Gridion364: Piechart for Classification Results of Diamond (default)](../stats/pics/gridion364_default.diamond.piechart.jpeg)|**Gridion364: Piechart for Classification Results of Diamond (default)**. The diagram shows the three species classified with more than one per cent of reads assigned: Listeria monocytogenes (2.895%), Enterococcus faecalis (1.012%) and Limosilactobacillus fermentum (4,812%). 75.606% of the reads could not be assigned to a species, but other taxa and 15.676% of the reads could not be assigned at all.|
|![Promethion365: Piechart for Classification Results of Diamond (default)](../stats/pics/gridion364_default.diamond.piechart.jpeg)|**Promethion365: Piechart for Classification Results of Diamond (default).**|
|||

***Figure 1: Classification Results for Diamond, CS Even*** <br> <br>

The usage of the custom database [didn’t change a thing, changed everything, whatever → Verweis auf Anhang für Bilder]

Regarding the CS Log samples and the default database, Listeria monocytogenes is supposed to be the most abundant species in the sample. Diamond assigned 18.873% of reads of the GridION sample to that species. No other species could be accurately classified (Others: 69.076%), 12.051% of the reads are unclassified. Although the most abundant species can be identified using Diamond, the abundance does not come near the expected abundance [Table X]. [Similar, different, whatever] results can be observed for the PromethION sample.

|||
|:--|:--|
|![Gridion366: Piechart for Classification Results of Diamond (default)](../stats/pics/gridion366_default.diamond.piechart.jpeg)|**Gridion366: Piechart for Classification Results of Diamond (default)**. The only species with more than one per cent of reads assigned to is Listeria monocytogenes with 18.873%. 12.051% of the reads could not be assigned to any taxa, whereas 69.076% of the reads could not be assigned on species level or the corresponding species have an abundance below 1%.|
|![Promethion367: Piechart for Classification Results of Diamond (default)](../stats/pics/gridion364_default.diamond.piechart.jpeg)|**Promethion367: Piechart for Classification Results of Diamond (default).**|
|||

***Figure 2: Classification Results for Diamond, CS Log*** <br> <br>

The usage of the custom database [didn’t change a thing, changed everything, whatever → Verweis auf Anhang für Bilder]

An explanation for the poor results might be that Diamonds key features are pairwise alignments and frameshift alignments, the taxonomic classification is only considered as an output format. This might lead to poorer performance classifying the single reads.

Due to the relatively long runtime [Table Time], no specifications and different parameters are used. <br> <br>



#### Kaiju
|||
|:--|:--|
|![Gridion364: Piechart for Classification Results of Kaiju (default)](../stats/pics/gridion364_default.kaiju.piechart.jpeg)\label{kaiju364D}|**Gridion364: Piechart for Classification Results of Kaiju (default)**. The diagram is parted into ten pieces, whereby 40.786% of reads could not be assigned to a taxon on species level, 3.883% of the reads are therefore assigned to a species but with less than 1% abundance and 14.078% of the reads are unclassified. The three most abundant species are Lactobacillus fermentum, Enterococcus faecalis and Listeria monocytogenes with 12.503%, 10.269% and 9.322%, respectively. The abundances of Pseudomonas aeruginoa, Salmonella enterica, Escherichia coli and Staphylococcus aureus range between 1.104% and 4.151%.|
|![Promethion365: Piechart for Classification Results of Kaiju (default)](../stats/pics/promethion365_default.kaiju.piechart.jpeg)\label{kaiju365D}|**Promethion365: Piechart for Classification Results of Kaiju (default).** This diagram is as well parted into ten pieces, whereby 39.812% of reads could not be assigned to a taxon on species level, 3.786% of the reads are therefore assigned to a species but with less than 1% abundance and 16.391% of the reads are unclassified. The three most abundant species are Lactobacillus fermentum, Enterococcus faecalis and Listeria monocytogenes with 12.033%, 9.956% and 9.046%, respectively. The abundances of Pseudomonas aeruginosa, Salmonella enterica, Escherichia coli and Staphylococcus aureus range between 1.111% and 3.98%.|
|||

***Figure 3: Classification Results for Kaiju, CS Even*** <br> <br>


The other protein-based classifier used in this comparison is Kaiju. Considering the CS Even samples, Kaiju is able to identify seven of the ten species in both samples and the abundances are similar as well. 3.883% and 3.786% of reads could not be classified at all for GridION and PromethION, respectively and roughly 40% of the reads in both samples could not be assigned on the species level, therefore roughly 3.8% of the reads are assigned to species that do not reach the 1% abundance mark (Tabelle Y). The plots produced on Kaiju outputs include an entry for the percentage of reads that could not be assigned to any taxa on species level due to the way Kaiju generates outputs, see \ref{kaiju364D} and \ref{kaiju365D}. 
The identified species are Lactobacillus fermentum, Enterococcus faecalis, Listeria monocytogenes, Staphylococcus aureus, Escherichia coli, Salmonella enterica and Pseudomonas aeruginosa. The default database does not include fungi, therefore the species that is not classified, although present in the reference database, is Bacillus subtilis. 

| Classified species 	| L. monocytogenes 	| E. faecalis 	| S. aureus 	| S. enterica 	| E. coli 	| P. aeruginosa 	| L. fermentum 	|   	| unclassified 	| others 	|     different taxon level   	|
|--------------------	|------------------	|-------------	|-----------	|-------------	|---------	|---------------	|--------------	|---	|--------------	|--------	|--------	|
| CS Even            	|                  	|             	|           	|             	|         	|               	|              	|   	|              	|        	|        	|
| GridION 364        	| 9.322            	| 10.269      	| 4.151     	| 1.779       	| 2.124   	| 1.104         	| 12.503       	|   	| 14.078       	| 3.883  	| 40.786 	|
| PromethION 365     	| 9.046            	| 9.956       	| 3.98      	| 1.784       	| 2.101   	| 1.111         	| 12.033       	|   	| 16.391       	| 3.786  	| 39.812 	|
| CS Log             	|                  	|             	|           	|             	|         	|               	|              	|   	|              	|        	|        	|
| GridION 366        	| 57.905           	| -           	| -         	| -           	| -       	| -             	| -            	|   	| 11.062       	| 3.389  	| 27.644 	|
| PromethION 367     	| 58.031           	| -           	| -         	| -           	| -       	| -             	| -            	|   	| 12.866       	| 3.135  	| 25.968 	|
|||

***Table 1: Abundances of classified species, Kaiju.*** The table shows the classificaiton results of Kaiju for all four samples considering the default database (in %). Note that the species that is present in the reference database but no classified is Bacillus subtilis. The two fungis can not be identified with the default databnase, because id only includes microbial genomes or proteomes. <br> <br>

The CS Log samples are similar as well.  Kaiju is able to assign 57.905% and 58.031% of the reads to Listeria monocytogenes, depending on the sequencing machine (GridION, PromethION). Roughly 11% and 12.866% of the reads could not be assigned at all, whereas 27.644% and 25.968% could not be assigned to a taxon on species level, respectively. Around 3% of the reads are assigned to species with less than 1% abundance, see \ref{kaiju364D} and \ref{kaiju365D}. 

|||
|:--|:--|
|![Gridion366: Piechart for Classification Results of Kaiju (default)](../stats/pics/gridion366_default.kaiju.piechart.jpeg)\label{kaiju366D}|**Gridion364: Piechart for Classification Results of Kaiju (default)**.  It is visible that the majority of reads is assigned to Listeria monocytogenes with 57.905%. Most of the remaining reads (27.644%) could not be assigned to anything on species level, therefore 3.389% of the reads are assigned to a species, but this species does not reach the abundance of 1%. 11.062% of the reads are unclassified.|
|![Promethion367: Piechart for Classification Results of Kaiju (default)](../stats/pics/promethion367_default.kaiju.piechart.jpeg)\label{kaiju367D}|**Promethion365: Piechart for Classification Results of Kaiju (default).** It is visible that the majority of reads is assigned to Listeria monocytogenes with 58.031%. Most of the remaining reads (25.968%) could not be assigned to anything on species level, therefore 3.135% of the reads are assigned to a species, but this species does not reach the abundance of 1%. 12.866% of the reads are unclassified.|
|||

***Figure 4: Classification Results for Kaiju, CS Log*** <br> <br>

#### CCMetagen
CCMetagen uses the KMA for aligning, which is designed to map reads against redundant databases. The tool is supposed to work for large datasets, however, no classification could be done for the deep sequences samples with PromethION. KAM throws an error stating not enough space on the device. Therefore, there are only one CS Even and one CS Log sample to analyse.
|||
|:--|:--|
|![Gridion364: Piechart for Classification Results of CCmetagen (default)](../stats/pics/gridion364_default.ccmetagen.piechart.jpeg)\label{ccmetagen367D}|**Gridion364: Piechart for Classification Results of CCMetagen (default).**  26.736% of reads couöd not be assigned to any taxon, whereas 19.458% of reads are not assigned to a taxon on species level or the species do not reach 1% abundance. The identified species are Enterococcus faecalis (1.795%), Escherichia coli (2.069%), Pseudomonas aeruginosa (3.387%), Limosilactobacillus fermentum (9.083%), Staphylococcus aureus (9.837%), Listeria monocytogenes (11.326%) and Bacillus spizizenii (16.309%).|
|||

***Figure X: Classification Results for CCMetagen, CS Even, GridION*** <br> <br>

CCMetagen is not able to classify 26.736% of the reads of CS Even and 19.458% of the reads could not be assigned to a taxon on species level. The remaining reads are assigned to species with abundances between 1.795% (Enterococcus faecalis) and 16.309 (Bacillus spizizenii). In general, CCMetagen is able to classify 5 species correctly (Figure). Limosilactobacillus fermentum and Bacillus spizizenii are, however, close relatives to Lactobacillus fermentum and Bacillus subtilis [QUELLE]. Again, the default databse does not include fungal genomes, therefore those cannot be considered here.

Considering the CS Log sample sequenced with GridION, CCMetagen is able to assign 71.494% of reads to Listeria monocytogenes and 2.822% to Pseudomonas aeruginosa. 0.279% are assigned to others and 25.405% are unclassified.

|||
|:--|:--|
|![Gridion366: Piechart for Classification Results of CCmetagen (default)](../stats/pics/gridion366_default.ccmetagen.piechart.jpeg)\label{ccmetagen367D}|**Gridion366: Piechart for Classification Results of CCMetagen (default).**  26.736% of reads couöd not be assigned to any taxon, whereas 19.458% of reads are not assigned to a taxon on species level or the species do not reach 1% abundance. The identified species are Enterococcus faecalis (1.795%), Escherichia coli (2.069%), Pseudomonas aeruginosa (3.387%), Limosilactobacillus fermentum (9.083%), Staphylococcus aureus (9.837%), Listeria monocytogenes (11.326%) and Bacillus spizizenii (16.309%).|
|||

***Figure X: Classification Results for CCMetagen, CS Log, GridION*** <br> <br>

<br> <br>

#### Centrifuge
For the CS Even samples, Centrifuge is able to classify 89.504% and 87.086% for GridION364 and PromethION365, respectively. Between 3.5% and 3.9% of the reads could not be assigned to a taxon on species level. 
Since the default database of Centrifuge does not contain fungal genomes, Centrifuge is only able to identify the eight bacterial species. Those species are identified with abundances ranging between 6% for Salmonella enterica and 18.368% for Bacillus substilis for GridION and between 5.936% for Salmonella enterica and 17.724% for Bacillus subtilis for PromethION, respectively (see Table 2). The classification results therefore do not improve with greater sequencing depth. 

|||
|:--|:--|
|![Gridion364: Piechart for Classification Results of Centrifuge (default)](../stats/pics/gridion364_default.centrifuge.piechart.jpeg)\label{centrifuge364D}|**Gridion364: Piechart for Classification Results of Centrifuge (default)**. Centrifuge is able to identify all bacterial species in the sample with relatively high abundances (6% to 18.368%). 10.496% of the reads could not be classified and 3.541% could not be assigned to a taxon on species level or exceed the 1% abundance mark.|
|![Promethion365: Piechart for Classification Results of Centrifuge (default)](../stats/pics/promethion365_default.centrifuge.piechart.jpeg)\label{centrifuge365D}|**Promethion365: Piechart for Classification Results of Centifuge (default).** Centrifuge is able to identify all bacterial species in the sample with relatively high abundances (5.936% to 17.724%). 12.914% of the reads could not be classified and 3.974% could not be assigned to a taxon on species level or exceed the 1% abundance mark.|
|||

***Figure 5: Classification Results for Centrifuge, CS Even*** <br> <br>

| Classified species 	| B. subtilis 	| L. monocytogenes 	| E. faecalis 	| S. aureus 	| S. enterica 	| E. coli 	| P. aeruginosa 	| L. fermentum 	|   	| unclassified 	| other 	|
|--------------------	|-------------	|------------------	|-------------	|-----------	|-------------	|---------	|---------------	|--------------	|---	|--------------	|-------	|
| CS Even            	|             	|                  	|             	|           	|             	|         	|               	|              	|   	|              	|       	|
| GridION 364        	| 18.368      	| 13.514           	| 11.182      	| 11.244    	| 6           	| 5.933   	| 5.21          	| 14.513       	|   	| 10.496       	| 3.541 	|
| PromethION 365     	| 17.724      	| 13.018           	| 10.803      	| 10.782    	| 5.936       	| 5.886   	| 5.204         	| 13.759       	|   	| 12.914       	| 3.974 	|
| CS Log             	|             	|                  	|             	|           	|             	|         	|               	|              	|   	|              	|       	|
| GridION 366        	| 1.085       	| 84.591           	|     -        	|    -       	|     -        	|       -  	| 4.653         	|      -        	|   	| 7.214        	| 2.457 	|
| PromethION 367     	| 1.069       	| 82.068           	|      -       	|   -        	|       -      	|      -   	| 4.532         	|       -       	|   	| 9.649        	| 2.682 	|
|||

***Table 2: Abundances of classified species, Centrifuge.*** The table shows the classificaiton results of Centrifuge for all four samples considering the default database (in %). TEXT TEXT TEXT. <br> <br>

The CS Log results show similarity betweent the samples as well. Three species can be identified with the majotrity of reads assigned to Listeria monocytogenes (84.591% and 82.068% for GridIOn and PromethION, respectively). Centrifuge assigned about 1% of the reads to Bacillus subtilis and 4.5% to Pseudomonas aeruginosa. The sample sequences with GridION shows slightly less uncassified reads with 7.214% in contrast to 9.649% for PromethION. There are about 2.5% reads that could not be assigned to a taxon on species level (Table, Picture).

|||
|:--|:--|
|![Gridion366: Piechart for Classification Results of Centrifuge (default)](../stats/pics/gridion366_default.centrifuge.piechart.jpeg)\label{centrifuge364D}|**Gridion366: Piechart for Classification Results of Centrifuge (default)**. Centrifuge is able to identify all bacterial species in the sample with relatively high abundances (6% to 18.368%). 10.496% of the reads could not be classified and 3.541% could not be assigned to a taxon on species level or exceed the 1% abundance mark.|
|![Promethion367: Piechart for Classification Results of Centrifuge (default)](../stats/pics/promethion367_default.centrifuge.piechart.jpeg)\label{centrifuge365D}|**Promethion365: Piechart for Classification Results of Centifuge (default).** Centrifuge is able to identify all bacterial species in the sample with relatively high abundances (5.936% to 17.724%). 12.914% of the reads could not be classified and 3.974% could not be assigned to a taxon on species level or exceed the 1% abundance mark.|
|||

[Results Custom Database]
[Results Restricted Run]
#### Next Tool
#### Next Tool
#### Next Tool
#### Next Tool
### Stuff that didn't work
## Conclusion
# Attachments and Supplementary Information
# Citations