# Project Module / Master Thesis

Benchmarking different classification tools for their usability on metagenomic long reads.

## How to get started
0. You need conda and snakemake
1. After installation, alter the config file for your needs and download the necessesities (indices, databases)
   - path to this directory
   - paths for the different databases, default and custom (you can add more) 
   - the locations of fastq files is needed
   - species of groudn truth
   - It's best to move this directory into <tt>results/</tt>, otherwise paths need to be adjusted
2. Call <tt>snakemake create</tt> to generate the project structure
3. Now you can either build custom databases or start with the default databases (change [line 12](Snakefile "Snakefile") accordingly to "default")
   - for custom databases, you can orientate yourself on the [Snakefile_DB](Snakefile_DB "Snakefile_DB) file
     - change the paths accordingly
4. run with <tt>snakemake --use-conda -j threads</tt>

## Tools
### Classificaiton Tools
|     Tool     |   Version  |   Type  |         Approach        |                       Reference                      |
|:------------:|:----------:|:-------:|:-----------------------:|:----------------------------------------------------:|
|   Diamond    | 2.0.5     | Protein |        Alignment        | http://www.diamondsearch.org/index.php               |
|     Kaiju    |    1.7.4   | Protein |   FM-Index, Alignment   |               http://kaiju.binf.ku.dk/               |
|   CCMetagen  |    1.2.3   |   DNA   |                         |       https://github.com/vrmarcelino/CCMetagen       |
|  Centrifuge  |    1.0.4   |   DNA   |         FM-Index        | https://ccb.jhu.edu/software/centrifuge/manual.shtml |
|     CLARK    |    1.2.5   |   DNA   |      (spaced) k-mer     |           http://clark.cs.ucr.edu/Overview/          |
|    Kraken2   | 2.0.7-beta |   DNA   |          k-mer          |         http://ccb.jhu.edu/software/kraken2/         |
### Others
|Tools|Version|Reference|
|:-------:|:-------:|:-------:|
|conda|4.7.5|https://docs.anaconda.com/|
|snakemake|3.10.0|https://snakemake.readthedocs.io/en/stable/|

## Conclusion
This research aimed to benchmark and compare different classification tools regarding their usability for metagenomic long-read data. For this, four nanopore samples based on the Zymo Community Standards are analysed using six tools mostly successful (Diamond, Kaiju, CCmetagen, Centrifuge, CLARK, Kraken2) and evaluation of the outcomes is done using common metrics like Area Under Precision-Recall Curve, Abundance Profile Similarities as well as runtime consumption. For this purpose, the generated output files are formated into a universal format which is then used to process the data regarding the metrics. Additionally, the difficulties of several tools are discussed.<br>
The evaluation revealed that Kraken2, Centrifuge and CLARK promise the best results for this dataset. At least for the used default database, the tools achieve good results considering the metrics and classification results themselves. Although there is deterioration with the custom database, those tools still achieve comparably good results. CLARK, however, might have trouble with building the needed indices due to memory limitations. CCMetagen is able to identify the present species, but the metrics show poorer results than the other DNA-based tools. A database building for the custom database is not possible. Regarding the protein-based tools, Kaiju performs better than Diamond and achieves, for the custom database, similar results than Centrifuge and Kraken2. Diamond is not able to identify the species in the dataset with appropriate abundances. <br>
It is possible that BugSeq might become a valuable tool for classification once the smaller bugs are fixed. <br> 
The validation using Multi Locus Sequence Types showed the expected results and it is able to assign the gene fragments to reads in the sample. <br>
It has to be considered that the scope of this project is rather small due to the limited number of samples and databases as well as the number of successfully working tools. Therefore, a similar comparison but with several datasets might ensure more reliable and accurate outcomes regarding the metrics.



