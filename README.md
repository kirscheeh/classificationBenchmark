# Project Module / Master Thesis

Benchmarking different classification tools for their usability on metagenomic long reads.

## Tools
### Classificaiton Tools
|     Tool     |   Version  |   Type  |         Approach        |                       Reference                      |
|:------------:|:----------:|:-------:|:-----------------------:|:----------------------------------------------------:|
|     Kaiju    |    1.7.4   | Protein |   FM-Index, Alignment   |               http://kaiju.binf.ku.dk/               |
|    Kraken2   | 2.0.7-beta |   DNA   |          k-mer          |         http://ccb.jhu.edu/software/kraken2/         |
|  Centrifuge  |    1.0.4   |   DNA   |         FM-Index        | https://ccb.jhu.edu/software/centrifuge/manual.shtml |
|    taxMaps   |     0.2    |   DNA   |         FM-Index        |          https://github.com/nygenome/taxmaps         |
| DeepMicrobes |git rev. 43b654b  |DNA| Machine Learning, k-mer |      https://github.com/MicrobeLab/DeepMicrobes      |
|  MetaOthello |git rev. 15ded5e  |DNA|          k-mer          |         https://github.com/xa6xa6/metaOthello        |
|    k-SLAM    |     1.0    |   DNA   |          k-mer          |            https://github.com/aindj/k-SLAM           |
|     CLARK    |    1.2.5   |   DNA   |      (spaced) k-mer     |           http://clark.cs.ucr.edu/Overview/          |
|   CCMetagen  |    1.2.3   |   DNA   |                         |       https://github.com/vrmarcelino/CCMetagen       |
|   Diamond    | 0.9.14     | Protein |        Alignment        | http://www.diamondsearch.org/index.php               |
| NBC           |           | DNA | |http://nbc.ece.drexel.edu/|
|CAT and BAT| 5.1.2| Protein/DNA||https://github.com/dutilh/CAT| 
### Others
|Tools|Version|Reference|
|:-------:|:-------:|:-------:|
|conda|4.7.5|https://docs.anaconda.com/|
|snakemake|3.10.0|https://snakemake.readthedocs.io/en/stable/|

## Metrics
- AUPR -- Area under Precision-Recall-Curve
  - Precision: Proportion of TP species identified in the sample divided by the number of total species identified by the method.
  - Recall: Proportion of TP species identifies in the sample divided by number of distinct species actually in the sample.
- Abundace Profile Similarity
- Runtime, Database Size, Memory


