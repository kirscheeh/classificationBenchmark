# Introduction
# Material and Methods
<!-- conda und snakemake erwähnen-->
## Preprocessing
## Classification
Classificaton describes the process of identifying the taxon of a given species [1]. blah

Common approaches to solve this task k-mer based algorithms or algorithm based on the FM-Index. Explanation here about these two methods, maybe a short explanation of the ML approach?
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
|    k-SLAM    |     1.0    |   DNA   |Alignment, k-mer          |            https://github.com/aindj/k-SLAM           |
| MegaBLAST???| | DNA| Alignment||
|  MetaOthello |git rev. 15ded5e  |DNA|          k-mer          |         https://github.com/xa6xa6/metaOthello        |
| NBC           |           | DNA | |http://nbc.ece.drexel.edu/|
|    taxMaps   |     0.2    |   DNA   |         FM-Index        |          https://github.com/nygenome/taxmaps         |

#### Protein-Level Classification
##### Diamond
##### Kaiju
<tt>Kaiju</tt> [Kaiju]() is a fast and sensitive tool for taxonomic classification of metagenomic samples that uses a reference-database of annotated protein-coding genes of microbial genomes. The DNA reads are translated into the six reading frames and split according to the stop codons. The resulting fragments are sorted regarding their length and due to the usage of the Ferragina and Mazini-Index (FM-Index), exact matches can be searched between read and database-reference in effient time [Kaiju]().
The used index <tt>kaiju_db_refseq_2020-05-25</tt> was downloaded from <tt>http://kaiju.binf.ku.dk/server</tt> as of 28/11/2020.

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
<tt>CLARK</tt>[clark]() is a taxonomic classification tool for metagenomic samples of any format (reads, contigs, scaffolds, assemblies, ...). The method is based on discriminative *k*-mers which is used in supervised sequence classification. <br>
The bacterial (and virus) databse was build using the script <tt>set_targets.sh</tt> as of 7/12/2020.

    CLARK -k INT (--long) -m 0 -O {input} -R {output} -D {databse}
    
    # Parameters
        # -k        k-mer size, has to be between 2 and 32, default:31 
        # --long    for long reads (only for full mode)
        # -m        mode of execution

##### DeepMicrobes
##### Kraken2
The taxonomic sequence classifier <tt> Kraken2 </tt> [Kraken2]() examines *k*-mers of a query sequence and uses those information to query a database. During the query, the *k*-mers are mapped to the lowest common ancestor of the genomes that contain a given *k*-mer [Kraken2](). <br>
??? Ich will die bestehende DB nutzen, aber da steht nicht wie und woher die kam ???

    kraken2 (--confidence X) --db kraken2-database --unclassified-out FILENAME_UN --report REPORT_NAME --output {output} {input}

    # Parameters 
        # --confidence          threshold that must be in [0,1]
        # --unclassified-out    prints unclassified sequences to filename
        # --classified-out      prints classified sequences to filename
        # --output              prints output to filename
        # --report              prints report with aggregate counts/cladde to file
        
##### k-SLAM
<tt> k-SLAM</tt> [kslam]() uses an alignment based approach for metagenomic analysis. To built thes alignments, a *k*-mer based approach s use. The found alignments of reads and genome are validated by using the Smith-Waterman algorithm. By identifying the lowest common ancestor, the taxonomy of the sample is concluded [kslam](). <br>
A database of bacteria was built using the <tt>install_slam.sh</tt> script as of 28/11/2020.

    SLAM --db {databse} (--min-alignment-score INT) --output-file {output} {input}

    # Parameters
        # --db                      database file
        # --min-alignment-score     alignment score cutoff

##### MegaBLAST ???
##### MetaOthello
##### NBC
##### taxMaps
<tt>taxMaps</tt> [taxMaps]() is a classification tool designed for short read metagenomic samples. It consists of several steps preceding the actual task of taxonomic classification. There is the preprocessing with quality trimming and adapter cutting as well as mapping. Here, only the taxonomic classification is done. The approach is based on the FM-Index [taxMaps](). <br> <!-- Index last edited: 06/03/2018-->
A pre-built index (refseq_complete_bacarchive) is used which was downloaded from <tt>ftp://ftp.nygenome.org/taxmaps/Indexes/</tt> as of 27/11/2020. The taxonomy table was downloaded from there as well.

    taxMaps -f {input} -t taxonomy.tbl.gz -d taxmaps/*.gem.* --cov -o {output}

    # Parameters
        # -f        input fastq
        # -l        in preprocessing: minimum read length for mapping
        # -C        in preprocessing: entropy cutoff for low complexity filtering
        # -d        index files
        # -t        taxonomic rable
        # --cov     coverage histogram
        # -o        output directory
        

### Metrics
#### Area-Under-Precision-Recall Curve
#### Abundace Profile Similarity
#### Computational Requirements
# Results and Discussion
# Conclusion
# Additional Information

# Sources
<!-- APA -->
[[1]](https://doi.org/10.1016/j.cell.2019.07.010) Simon, H. Y., Siddle, K. J., Park, D. J., & Sabeti, P. C. (2019). Benchmarking metagenomics tools for taxonomic classification. *Cell*, 178(4), 779-794.

[Kaiju](https://doi.org/10.1186/s13062-018-0208-7) Menzel, P., Ng, K. L., & Krogh, A. (2016). Fast and sensitive taxonomic classification for metagenomics with Kaiju. *Nature communications*,* 7(1), 1-9.

[Kraken2](https://doi.org/10.1186/s13059-019-1891-0) Wood, D. E., Lu, J., & Langmead, B. (2019). Improved metagenomic analysis with Kraken 2. *Genome biology*, 20(1), 257.

[taxMaps](http://www.genome.org/cgi/doi/10.1101/gr.225276.117) Corvelo, A., Clarke, W. E., Robine, N., & Zody, M. C. (2018). taxMaps: comprehensive and highly accurate taxonomic classification of short-read data in reasonable time. *Genome research*, 28(5), 751-758.

[kslam](https://doi.org/10.1093/nar/gkw1248) Ainsworth, D., Sternberg, M. J., Raczy, C., & Butcher, S. A. (2017). k-SLAM: accurate and ultra-fast taxonomic classification and gene identification for large metagenomic data sets. *Nucleic acids research*, 45(4), 1649-1656.

[clark](https://doi.org/10.1186/s12864-015-1419-2) Ounit, R., Wanamaker, S., Close, T. J., & Lonardi, S. (2015). CLARK: fast and accurate classification of metagenomic and genomic sequences using discriminative k-mers. *BMC genomics*, 16(1), 236.