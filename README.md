# Projektarbeit

## Literaturrecherche: Tools
- Kraken(2) 2014(2019)
- MegaBLAST 2008
- Bracken 2017
- CLARK-S 2016
- Taxonomer http://taxonomer.com/ --> pathogen detection and host mRNA expression profiling
- taxMaps --> short reads
- MetaOthello 2017
- k-SLAM 2016
- NBC 2010libre

## Literaturrecherche: Maße zum Vergleich der Tools
- Aus dem Benachmark-Paper (Simon H. Ye et. al, 2019)
  - Custom Database, Memory Required, Time Required
  - Precision (Proportion of TP species in the sample divided by number of distinct species actually in the sample) and Recall --> Precision-Recall curve --> AUPR
    - AUPR is biased towars low-precision, high-recall classifiers
  - F1-Score?
  - ROC Curves are less informative in this context because false negatives are poorly identified here
  -  it is also important to evaluate how accurately the abundance of each species or genera in the resulting classification reflects the abundance of each species in the original biological sample (‘‘ground truth’’)
  -  Abundance can be consid-ered either as the relative abundance of reads from each taxa(‘‘raw’’) or by inferring abundance of the number of individualsfrom each taxa by correcting read counts for genome size (‘‘cor-rected’’). --> some 
