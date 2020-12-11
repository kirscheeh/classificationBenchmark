# Introduction
# Material and Methods
<!-- conda und snakemake erwähnen-->
## Preprocessing
## Classification
Classificaton describes the process of identifying the taxon of a given species [1]. blah

Common approaches to solve this task k-mer based algorithms or algorithm based on the FM-Index.
### Tools
|     Tool     |   Version  |   Type  |         Approach        |                       Reference                      |
|:------------:|:----------:|:-------:|:-----------------------:|:----------------------------------------------------:|
|   Diamond    | 0.9.14     | Protein |        Alignment        | http://www.diamondsearch.org/index.php               |
|     Kaiju    |    1.7.4   | Protein |   FM-Index, Alignment   |               http://kaiju.binf.ku.dk/               |
|CAT and BAT| 5.1.2| Protein/DNA||https://github.com/dutilh/CAT| 
|   CCMetagen  |    1.2.3   |   DNA   |                         |       https://github.com/vrmarcelino/CCMetagen       |
|  Centrifuge  |    1.0.4   |   DNA   |         FM-Index        | https://ccb.jhu.edu/software/centrifuge/manual.shtml |
|     CLARK    |    1.2.5   |   DNA   |      (spaced) k-mer     |           http://clark.cs.ucr.edu/Overview/          |
| DeepMicrobes |git rev. 43b654b  |DNA| Machine Learning, k-mer |      https://github.com/MicrobeLab/DeepMicrobes      |
|    Kraken2   | 2.0.7-beta |   DNA   |          k-mer          |         http://ccb.jhu.edu/software/kraken2/         |
|    k-SLAM    |     1.0    |   DNA   |          k-mer          |            https://github.com/aindj/k-SLAM           |
| MegaBLAST???| | DNA| Alignment||
|  MetaOthello |git rev. 15ded5e  |DNA|          k-mer          |         https://github.com/xa6xa6/metaOthello        |
| NBC           |           | DNA | |http://nbc.ece.drexel.edu/|
|    taxMaps   |     0.2    |   DNA   |         FM-Index        |          https://github.com/nygenome/taxmaps         |


#### Protein-Level Classification
##### Diamond
##### Kaiju
<tt>Kaiju</tt> [Kaiju]() is a fast and sensitive tool for taxonomic classification of metagenomic samples that uses a reference-database of annotated protein-coding genes of microbial genomes. The DNA reads are translated into the six reading frames and split according to the stop codons. The resulting fragments are sorted regarding their length and due to the usage of the Ferragina and Mazini-Index (FM-Index), exact matches can be searched between read and database-reference in effient time [Kaiju]().

    kaiju -t nodes.dmp -f kaiju_db_refseq.fmi -i {input} -o {output} -m INT -E FLOAT
    
    # Parameters
        # -t    name of nodes.dmp file
        # -f    name of database (.fmi) file
        # -i    input file containing fasta/fastq
        # -o    name of output file
        # -m    minimum match length (default: 11)
        # -E    minimum e-value in Greedy mode (default)

#### DNA-Level Classification
##### CAT and BAT
##### CCMetagen
##### Centrifuge
##### CLARK
##### DeepMicrobes
##### Kraken2
##### k-SLAM
##### MegaBLAST ???
##### MetaOthello
##### NBC
##### taxMaps
### Metrics
#### Area-Under-Precision-Recall Curve
#### Abundace Profile Similarity
#### Computational Requirements
# Results and Discussion
# Conclusion
# Additional Information

# Sources
[[1]](https://doi.org/10.1016/j.cell.2019.07.010) Simon, H. Ye, et al. "Benchmarking metagenomics tools for taxonomic classification." Cell 178.4 (2019): 779-794. <!-- [[1]](https://doi.org/10.1016/j.cell.2019.07.010 "Simon, H. Ye, et al. "Benchmarking metagenomics tools for taxonomic classification." Cell 178.4 (2019): 779-794.")-->

[Kaiju](https://doi.org/10.1186/s13062-018-0208-7) Menzel, Peter, Kim Lee Ng, and Anders Krogh. "Fast and sensitive taxonomic classification for metagenomics with Kaiju." Nature communications 7.1 (2016): 1-9.