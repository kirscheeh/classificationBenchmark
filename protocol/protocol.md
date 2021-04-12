# Introduction
# Material and Methods
# Data -- Mock Community
- CSS, Abkürzung CS Even und CS Log einführn
- Dataset erklären, Spezies nennen, grobe Infos zu Spezies
- Abundances, soweit bekannt
<!-- conda und snakemake erwähnen-->
## Preprocessing
## Classification
Classificaton describes the process of identifying the taxon of a given species [1]. blah

Common approaches to solve this task k-mer based algorithms or algorithm based on the FM-Index. Explanation here about these two methods, maybe a short explanation of the ML approach?
### Tools
|     Tool     |   Version  |   Type  |         Approach        |Default Database|                       Reference                      |
|:------------:|:----------:|:-------:|:-----------------------:|:---:|:----------------------------------------------------:|
|   Diamond    | 2.0.5          | Protein |        Alignment       | full Proteome Bacteria|http://www.diamondsearch.org/index.php               |
|     Kaiju    |    1.7.4        | Protein |   FM-Index, Alignment  | |              http://kaiju.binf.ku.dk/               |
|   CCMetagen  |    1.2.3        |   DNA   |*k*-mer, Alignment (KMA)|  |     https://github.com/vrmarcelino/CCMetagen       |
|  Centrifuge  |    1.0.4        |   DNA   |         FM-Index       | |https://ccb.jhu.edu/software/centrifuge/manual.shtml |
|     CLARK    |    1.2.5        |   DNA   |      (spaced) *k*-mer  |  |         http://clark.cs.ucr.edu/Overview/          |
|    Kraken2   | 2.0.7-beta      |   DNA   |          *k*-mer          ||         http://ccb.jhu.edu/software/kraken2/         |
|BugSeq| v1 | DNA | Pipeline?? || https://bugseq.com/free |
#### Protein-Level Classification
##### Diamond
This tool is a sequence aligner for protein and translated DNA searches specifically designed for big sequence data. <br>
The database was created on 14/12/2020 with the <tt>diamond makedb</tt> command and sequences downloaded on 27/7/2019 (genomes/bacteria...)

    diamond blastx --db {database} -g {input} --taxonlist {database_list} -o {output}

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
##### CCMetagen
This classifier uses a *k*-mer alignment (KMA) [kma]() mapping method and produces ranked taxonomic classification results [ccmetagen]().<br>
The used indexed database <tt>ncbi_nt_kma</tt> was downloaded from <tt>http://www.cbs.dtu.dk/public/CGE/databases/CCMetagen/</tt> as of 08/12/2020.

    CCMetagen.py  -o {output} -r RefSeq -i {database} -ef FLOAT -c INT
    
    # Parameters    
        # -r    reference database
        # -i    path to kma result
        # -ef   extended output file that includes percentage of classified reads
        # -c    minimum coverage of the reference sequence

##### Centrifuge
<tt>Centrifuge</tt> [centrifuge]() is a classification tool for metagenomic microbial data. This FM-Index-based approach searches for forward and reverse complements of the given input reads in the corresponding database of species. If a match with a given seed length is found, that region is expanded until a mismatch is found [centrifuge](). <br>
The used indices <tt>b_compressed</tt> are downloaded from <tt>ftp://ftp.ccb.jhu.edu/pub/infphilo/centrifuge/data/old-indices/</tt> as of 12/09/2019.

    centrifuge -f -x INDEX_FILE {input} --report-file LOCATION_OF_REPORT --min-hitlen INT -S {output}
        # -q 				files are fastq
    	# -x 				index files
    	# --report-file 	generated report file
    	# -S 				output file
        # --min-hitlen      minimum length of partial hits (default: 22)
<!--  # -f                query input files are (multi)fasta -->
        
##### CLARK
<tt>CLARK</tt>[clark]() is a taxonomic classification tool for metagenomic samples of any format (reads, contigs, scaffolds, assemblies, ...). The method is based on discriminative *k*-mers which is used in supervised sequence classification. <br>
The bacterial (and virus) databse was build using the script <tt>set_targets.sh</tt> as of 7/12/2020.

    CLARK -k INT (--long) -m 0 -O {input} -R {output} -D {databse}
    
    # Parameters
        # -k        k-mer size, has to be between 2 and 32 (default: 31)
        # --long    for long reads (only for full mode)
        # -m        mode of execution

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
        


##### NBC
The <tt>NBC</tt> taxonomic classifier implemented the naïve bayes classifier for metagenomic samples. These classifiers are based on the Bayes theorem. This tool is used as a webserver with <tt>http://nbc.ece.drexel.edu/</tt>


#### Others
- snakemake
- R
- conda
- Python
- Bash
  
### Metrics
Introduction on diffivulties regarding the comparison of different tools with differents databases etc

#### Area-Under-Precision-Recall Curve
The Area-Under-Precision-Recall curve (AUPR) is a metric that combines the most important measures for metagenomic classification: precision and recall [[1]](). Precision is defined as $precision=\frac{TP}{TP+FP}$, i.e. the ratio between true positive (TP) classification results and the total numer of classification results that are reported as true, inclusing falsly positive (FP) hits. Recall or sensitivity, on the other hand, is defined as the ratio of true positives against all correct classifications including false negatives (FN), i.e. $recall=\frac{TP}{TP+FN}$. <br>
The AUPR curve can be used to evaluate precision and recall across different abundance thresholds. If the threshold are chosen accordingly in the range from 0-1.0, the AUPR returns a single metric considering precision and recall. In short: This metric considers the number of correctly identified species [[1]]().
For this metric, a ground-truth is needed.
- and the information here that i used a script to calculate this
- list the way how the information was retrieved for the different tools

#### Abundace Profile Similarity
#### Computational Requirements
Additionally to the quality of the different classifiers, the computational requirements are compared, i.e. the runtime and amount of memory. They are measured using the <tt>benchmark</tt> option in <tt>snakemake</tt>, which returns the wall clock time of a task and the memory usage in MiB.
# Results and Discussion
## Installation: Usability
### Unused Tools
## CS Even
### Protein-Level Classification
#### Classification Results Diamond
#### Classification Results Kaiju
### DNA-Level Classification
#### Classification Results Kraken2
#### Classification Results Centrifuge
#### Classification Results CLARK
#### Classification Results CCMetagen
## CS Log
### Protein-Level Classification
#### Classification Results Diamond
#### Classification Results Kaiju
### DNA-Level Classification
#### Classification Results Kraken2
#### Classification Results Centrifuge
#### Classification Results CLARK
#### Classification Results CCMetagen
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

[catbat](https://doi.org/10.1186/s13059-019-1817-x) von Meijenfeldt, F. B., Arkhipova, K., Cambuy, D. D., Coutinho, F. H., & Dutilh, B. E. (2019). Robust taxonomic classification of uncharted microbial sequences and bins with CAT and BAT. *Genome biology*, 20(1), 217.

[centrifuge](https://doi.org/10.1101%2Fgr.210641.116) Kim, D., Song, L., Breitwieser, F. P., & Salzberg, S. L. (2016). Centrifuge: rapid and sensitive classification of metagenomic sequences. *Genome research*, 26(12), 1721-1729.

[kma](https://doi.org/10.1186/s12859-018-2336-6) Clausen, P. T., Aarestrup, F. M., & Lund, O. (2018). Rapid and precise alignment of raw reads against redundant databases with KMA. *BMC bioinformatics*, 19(1), 1-8.

[ccmetagen](https://doi.org/10.1186/s13059-020-02014-2) Marcelino, V. R., Clausen, P. T., Buchmann, J. P., Wille, M., Iredell, J. R., Meyer, W., ... & Holmes, E. C. (2020). CCMetagen: comprehensive and accurate identification of eukaryotes and prokaryotes in metagenomic data. *Genome Biology*, 21(1), 1-15.

[metaothello](https://doi.org/10.1093/bioinformatics/btx432) Liu, X., Yu, Y., Liu, J., Elliott, C. F., Qian, C., & Liu, J. (2018). A novel data structure to support ultra-fast taxonomic classification of metagenomic sequences with k-mer signatures. *Bioinformatics*, 34(1), 171-178.

[nbc](https://doi.org/10.1093/bioinformatics/btq619) Rosen, G. L., Reichenberger, E. R., & Rosenfeld, A. M. (2011). NBC: the Naive Bayes Classification tool webserver for taxonomic classification of metagenomic reads. *Bioinformatics*, 27(1), 127-129.