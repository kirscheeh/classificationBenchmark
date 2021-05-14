### note ccmetagen 366: mapped:80.737475%

# TODO LIST

## kraken 2 git
  /home/re85gih/projectClassification/kraken2/kraken2
  /home/re85gih/projectClassification/kraken2/kraken2-build
  /home/re85gih/projectClassification/kraken2/kraken2-inspect

- more information on benchmarking
  - leave one taxa out approach aka clade exclusion
  - existing benchmarking datasets
  - --> they did three things: clade exclusion, high-complexity fold standard CAMI assembly and recently publisehd sequences
- https://www.zymoresearch.de/collections/zymobiomics-microbial-community-standards/products/zymobiomics-microbial-community-standard

- centrifuge
  - no difference if w/ or w/o -ignore-quals 

- kslam
  - without parameter for num_reads_at_once: bad alloc
  - parameter set as 1000000: runtime over 7days

- clark
  - 364 took so much time because of db built 
  - 1 day, 7:02:37.059451
taxmaps error
- gem-mapper: unrecognized option '--fast-mapping'
GEM-Mapper error:
> Option not recognized
- korrektur in taxMaps file
# Tools that did not work
## Lime
- Installation via git and make commands
- Error in Install_Preprocessing_Tools.sh due to denied permission
- tried to do it manually: egsa make did throw a error
<!--
git clone https://github.com/veronicaguerrini/LiME	
cd LiME	
one of the follwing two make thingys; they are for different approaches
make chose this one
make EBWT=0	
Install_Preprocessing_Tools.sh ging nicht (permission denied). Habs händisch versucht, Fehler bei egsa make; dont know why
-->
## Megan-LR
- page for this tool could not be found?!

## MetaMaps
- Installation instructions are bad
- conda: dependeny cpp-boost needed in correct version --> throw a lot of incompatabilities
  - UnsatisfiableError: The following specifications were found to be incompatible with each other:
  - conda-forge/linux-64::_openmp_mutex==4.5=1_gnu -> openmp_impl==9999
  - conda-forge/linux-64::boost-cpp==1.70.0=h7b93d67_3 -> libboost[version='<0']
  - conda-forge/linux-64::bzip2==1.0.8=h7f98852_4 -> libgcc-ng[version='>=9.3.0'] -> _openmp_mutex[version='>=4.5'] -> openmp_impl==9999
  - conda-forge/linux-64::libgcc-ng==9.3.0=h5dbcf3e_17 -> _openmp_mutex[version='>=4.5'] -> openmp_impl==9999
  - metamaps -> boost-cpp[version='>=1.70.0,<1.70.1.0a0'] -> libboost[version='<0']
  
## kslam
- appears to be able to deal with files up to 10.000.000 sequences, throws error (bad_alloc) for 2.4mil sequences nonetheless --> fixing with --num-reads-at-once
100 time: 
s	h:m:s
2365.960589170456	0:39:25.960589

## metaothello
segmentation fraud

## catbat
- seems to need contigs, not just long metagenomic sequences

# ccmetagen abundance
(KMA default depth, which is the number of nucleotides overlapping each template, divided by the lengh of the template)

# build commands for bac_fung.dmd
rule diamond_db:
    input: 
        faa="/mnt/fass1/kirsten/databases/diamond_all/faa/full_proteome_bacteria_scerevisiae_cneoformans.faa",
        map="/mnt/fass1/genomes/new_bacteria/bacteria_blast_db/prot_accession2taxid.txt",
        nodes="/mnt/fass1/kirsten/databases/diamond/nodes.dmp",
        names="/mnt/fass1/kirsten/databases/diamond/names.dmp"
    output:
        "/mnt/fass1/kirsten/databases/diamond_all/nr.dmnd"
    benchmark:
        "/mnt/fass1/kirsten/result/classification/benchmarks/diamond.db.benchmark.txt"
    conda:
        "envs/diamond.yaml"
    params:
        "/mnt/fass1/kirsten/databases/diamond_all/nr"
    threads: 8
    shell:
        "diamond makedb --in {input.faa} -d {params} --taxonmap {input.map} --taxonnodes {input.nodes} --taxonnames {input.names}"

time:
s	h:m:s
1929.9900908470154	0:32:09.990091


rule centrifuge_db:
    input:
        map = "/mnt/fass1/kirsten/databases/centrifuge_all/seqid2taxid.map",
        nodes = "/mnt/fass1/kirsten/databases/centrifuge_all/taxonomy/nodes.dmp",
        names ="/mnt/fass1/kirsten/databases/centrifuge_all/taxonomy/names.dmp",
        faa="/mnt/fass1/kirsten/databases/centrifuge_all/fna/full_bacteria_scerevisiae_cneoformans.fna"
    output:
       file1= "/mnt/fass1/kirsten/databases/centrifuge_all/bac_cer_neo.1.cf",
       file2= "/mnt/fass1/kirsten/databases/centrifuge_all/bac_cer_neo.2.cf",
       file3= "/mnt/fass1/kirsten/databases/centrifuge_all/bac_cer_neo.3.cf"
    threads: 8
    benchmark:
        "/mnt/fass1/kirsten/result/classification/benchmarks/centrifuge.db.benchmark.txt"
    params:
        "/mnt/fass1/kirsten/databases/centrifuge_all/bar_cer_neo"
    conda:
        "envs/centrifuge.yaml"
    shell:
        "centrifuge-build -p {threads} --conversion-table {input.map} --taxonomy-tree {input.nodes} --name-table {input.names} {input.faa} {params}"

time: 
s	h:m:s
97908.76425027847	1 day, 3:11:48.764250

### kma
piecer ccmetagen
start="$2"
end="$3"
sed -e "1,${start}d;${end}q" $1 > $2

#head -12000000 "$1" > "$2" 
#for i in {1..15} #12
#do
    start=$((12000000*i))
    end=$((start+12000000))
    sed -e "1,${start}d;${end}q" $1 > $2
#done

error: Error: 28 (No space left on device)


# FÜR CENTRIFUGE DB
seqid2taxid.map von kraken2 genutzt!

# diamond
promethion run failed after around two weeks
started around 04/03/2021, failed on 04/20/2021
/bin/bash: line 1:  9667 Aborted                 diamond blastx --db /mnt/fass1/kirsten/databases/diamond/nr -q /mnt/fass1/kirsten/data/promethion367.fastq -o /mnt/fass1/kirsten/result/classification/diamond/default/promethion367_default.diamond.classification -p 8 --log --outfmt 102

# 30.4
- diamond
- /bin/bash: line 1:  3480 Aborted                 diamond blastx --db /mnt/fass1/kirsten/databases/custom/diamond/refseqBacFung.diamond.dmnd -q /mnt/fass1/kirsten/data/gridion366.fastq -o /mnt/fass1/kirsten/result/classification/diamond/custom/gridion366_custom.diamond.classification -p 8 --outfmt 102
  
/bin/bash: line 1: 42886 Aborted

- kma db
/bin/bash: line 1: 15671 Killed                  kma_index -i /mnt/fass1/kirsten/databases/custom/ccmetagen/refseq_bac_fung.ccmetagen.fna -o /mnt/fass2/projects/kirsten/refseq_bac_fung.kma

### rest
- *Bacillus subtilis* https://pubmlst.org/bigsdb?db=pubmlst_bsubtilis_seqdef&page=schemeInfo&scheme_id=1
- *Listeria monocytogenes* https://bigsdb.pasteur.fr/cgi-bin/bigsdb/bigsdb.pl?db=pubmlst_listeria_seqdef&page=schemeInfo&scheme_id=2
  - https://bigsdb.pasteur.fr/cgi-bin/bigsdb/bigsdb.pl?db=pubmlst_listeria_seqdef&page=downloadProfiles&scheme_id=2
- *Enterococcus faecalis* https://pubmlst.org/bigsdb?db=pubmlst_efaecalis_seqdef&page=schemeInfo&scheme_id=1
- *Staphylococcus aureus* https://pubmlst.org/bigsdb?db=pubmlst_saureus_seqdef&page=schemeInfo&scheme_id=1
- *Salmonella enterica* https://pubmlst.org/bigsdb?db=pubmlst_mlst_seqdef&page=schemeInfo&scheme_id=2
- https://pubmlst.org/bigsdb?db=pubmlst_mlst_seqdef&page=downloadProfiles&scheme_id=2
- *Escherichia coli* https://bigsdb.pasteur.fr/cgi-bin/bigsdb/bigsdb.pl?db=pubmlst_ecoli_seqdef&page=schemeInfo&scheme_id=1
   - https://bigsdb.pasteur.fr/cgi-bin/bigsdb/bigsdb.pl?db=pubmlst_ecoli_seqdef&page=downloadProfiles&scheme_id=1
- *Pseudomonas aeruginosa* https://pubmlst.org/bigsdb?db=pubmlst_paeruginosa_seqdef&page=schemeInfo&scheme_id=1
- *Lactobacillus fermentum* parB, ychF, pyrG, atpF, recA, ileS, recG, and leuS https://link.springer.com/article/10.1007/s00203-017-1346-5 https://link.springer.com/article/10.1007/s00203-017-1346-5/tables/2
    - https://doi.org/10.1007/s00203-017-1346-5
    - 
    - https://static-content.springer.com/esm/art%3A10.1007%2Fs00203-017-1346-5/MediaObjects/203_2017_1346_MOESM1_ESM.docx

    - found in additional information
- *Saccharomyces cerevisiae*
  - ACC1, ADP1, GLN4, MET4, NUP116, and RPN2, https://link.springer.com/content/pdf/10.1007/s10068-018-0335-z.pdf
- *Cryptococcus neoformans* CAP59, GPD1, LAC1, PLB1, SOD1, URA5 and IGS1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2884100/
  - https://mlst.mycologylab.org/page/Allele_Search/30707
  - https://academic.oup.com/view-large/16644048
  - based on second links genes, the database of first link was used to get a sequence for each loci --> allele location 1




old 
Quellen

[Datta](https://doi.org/10.1007/s10311-020-01010-z) Datta, S., Rajnish, K. N., Samuel, M. S., Pugazlendhi, A., & Selvarajan, E. (2020). Metagenomic applications in microbial diversity, bioremediation, pollution monitoring, enzyme and drug discovery. A review. *Environmental Chemistry Letters*, 18(4), 1229-1241.

[weizhong](https://doi.org/10.1093/bib/bbs035) Li, W., Fu, L., Niu, B., Wu, S., & Wooley, J. (2012). Ultrafast clustering algorithms for metagenomic sequence analysis. *Briefings in bioinformatics*, 13(6), 656-668.

[ONT_lu](https://doi.org/10.1016/j.gpb.2016.05.004) Lu, H., Giordano, F., & Ning, Z. (2016). Oxford Nanopore MinION sequencing and genome assembly. *Genomics, proteomics & bioinformatics*, 14(5), 265-279.

[benchmark](https://doi.org/10.1016/j.cell.2019.07.010) Simon, H. Y., Siddle, K. J., Park, D. J., & Sabeti, P. C. (2019). Benchmarking metagenomics tools for taxonomic classification. *Cell*, 178(4), 779-794.

[conda](Anaconda Software Distribution. (2020). Anaconda Documentation. *Anaconda Inc.* Retrieved from https://docs.anaconda.com/)

[PRROC](https://cran.r-project.org/web/packages/PRROC/index.html) Jens Keilwagen, Ivo Grosse and Jan Grau (2014). Area under Precision-Recall Curves for Weighted and Unweighted Data. *PLOS ONE* (9) 3.

[DataPaper](https://doi.org/10.1093/gigascience/giz043) Nicholls, S. M., Quick, J. C., Tang, S., & Loman, N. J. (2019). Ultra-deep, long-read nanopore sequencing of mock microbial community standards. *Gigascience*, 8(5), giz043.

[Morgan2012](https://doi.org/10.1186/gb-2012-13-9-r79) Morgan, X. C., Tickle, T. L., Sokol, H., Gevers, D., Devaney, K. L., Ward, D. V., ... & Huttenhower, C. (2012). Dysfunction of the intestinal microbiome in inflammatory bowel disease and treatment. *Genome Biology*, 13(9), 1-18.

[ZymoEven](https://www.zymoresearch.de/collections/zymobiomics-microbial-community-standards/products/zymobiomics-microbial-community-standard) Zymo Research Corporation, Irvine, CA, USA. Product D6300, Lot ZRC190633

[ZymoLog](https://www.zymoresearch.de/collections/zymobiomics-microbial-community-standards/products/zymobiomics-microbial-community-standard-ii-log-distribution) Zymo Research Corporation, Irvine, CA, USA. Product D6310, Lot ZRC190842

[ccmetagen](https://doi.org/10.1186/s13059-020-02014-2) Marcelino, V. R., Clausen, P. T., Buchmann, J. P., Wille, M., Iredell, J. R., Meyer, W., ... & Holmes, E. C. (2020). CCMetagen: comprehensive and accurate identification of eukaryotes and prokaryotes in metagenomic data. *Genome biology*, 21, 1-15.

[Diamond](https://doi.org/10.1038/nmeth.3176) Buchfink, B., Xie, C., & Huson, D. H. (2015). Fast and sensitive protein alignment using DIAMOND. *Nature methods*, 12(1), 59-60.

[Kaiju](https://doi.org/10.1186/s13062-018-0208-7) Menzel, P., Ng, K. L., & Krogh, A. (2016). Fast and sensitive taxonomic classification for metagenomics with Kaiju. *Nature communications*, 7(1), 1-9.

[BugSeq](https://doi.org/10.1186/s12859-021-04089-5) Fan, J., Huang, S., & Chorlton, S. D. (2021). BugSeq: a highly accurate cloud platform for long-read metagenomic analyses. *BMC bioinformatics*, 22(1), 1-12.

[Centrifuge](https://doi.org/10.1101%2Fgr.210641.116) Kim, D., Song, L., Breitwieser, F. P., & Salzberg, S. L. (2016). Centrifuge: rapid and sensitive classification of metagenomic sequences. *Genome research*, 26(12), 1721-1729.

[PubMLST](https://pubmlst.org/multilocus-sequence-typing) Public databases for molecular typing and microbial genome diversity. Multi-Locus Sequence Typing. Retrieved from https://pubmlst.org/multilocus-sequence-typing. Last visited on 21/04/2021.

[MLSTToxi](https://www.sciencedirect.com/science/article/pii/S0580951715000148) Dingle, T. C., & MacCannell, D. R. (2015). Molecular strain typing and characterisation of toxigenic Clostridium difficile. *Methods in Microbiology*, 42, 329-357.

[MLSTfermentum](https://doi.org/10.1007/s00203-017-1346-5) Poluektova, E. U., Yunes, R. A., Epiphanova, M. V., Orlova, V. S., & Danilenko, V. N. (2017). The Lactobacillus rhamnosus and Lactobacillus fermentum strains from human biotopes characterized with MLST and toxin-antitoxin gene polymorphism. *Archives of microbiology*, 199(5), 683-690.

[MLSTcryptococcus](https://doi.org/10.1080/13693780902953886) Meyer, W., Aanensen, D. M., Boekhout, T., Cogliati, M., Diaz, M. R., Esposto, M. C., ... & Kwon-Chung, J. (2009). Consensus multi-locus sequence typing scheme for Cryptococcus neoformans and Cryptococcus gattii. *Medical mycology*, 47(6), 561-570.

[NCBISallmonella](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi)

[NBC](https://academic.oup.com/bioinformatics/article/27/1/127/202209) Rosen, G. L., Reichenberger, E. R., & Rosenfeld, A. M. (2011). NBC: the Naive Bayes Classification tool webserver for taxonomic classification of metagenomic reads. *Bioinformatics*, 27(1), 127-129.

[kslam](https://academic.oup.com/nar/article/45/4/1649/2674183) Ainsworth, D., Sternberg, M. J., Raczy, C., & Butcher, S. A. (2017). k-SLAM: accurate and ultra-fast taxonomic classification and gene identification for large metagenomic data sets. *Nucleic acids research*, 45(4), 1649-1656.

[lime](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-020-03628-w) Guerrini, V., Louza, F. A., & Rosone, G. (2020). Metagenomic analysis through the extended Burrows-Wheeler transform. *BMC bioinformatics*, 21(8), 1-25.

[taxmaps](https://genome.cshlp.org/content/28/5/751) Corvelo, A., Clarke, W. E., Robine, N., & Zody, M. C. (2018). taxMaps: comprehensive and highly accurate taxonomic classification of short-read data in reasonable time. *Genome research*, 28(5), 751-758.

[metaothello](https://doi.org/10.1093/bioinformatics/btx432) Liu, X., Yu, Y., Liu, J., Elliott, C. F., Qian, C., & Liu, J. (2018). A novel data structure to support ultra-fast taxonomic classification of metagenomic sequences with k-mer signatures. *Bioinformatics*, 34(1), 171-178.

[blast](https://doi.org/10.1016/S0022-2836(05)80360-2) Altschul, S. F., Gish, W., Miller, W., Myers, E. W., & Lipman, D. J. (1990). Basic local alignment search tool. *Journal of molecular biology*, 215(3), 403-410.

[MLST_Saccharomyces](https://doi.org/10.1007/s10068-018-0335-z) Eeom, Y. J., Son, S. Y., Jung, D. H., Hur, M. S., Kim, C. M., Park, S. Y., ... & Park, C. S. (2018). Diversity analysis of Saccharomyces cerevisiae isolated from natural sources by multilocus sequence typing (MLST). *Food science and biotechnology*, 27(4), 1119-1127.

[renamingFermentum](https://doi.org/10.1099/ijsem.0.004107) Zheng, J., Wittouck, S., Salvetti, E., Franz, C. M., Harris, H. M., Mattarelli, P., ... & Lebeer, S. (2020). A taxonomic note on the genus Lactobacillus: Description of 23 novel genera, emended description of the genus Lactobacillus Beijerinck 1901, and union of Lactobacillaceae and Leuconostocaceae. *International journal of systematic and evolutionary microbiology*, 70(4), 2782-2858.

[subSpecB]( https://doi.org/10.1007/s10482-019-01354-9) Dunlap, C. A., Bowman, M. J., & Zeigler, D. R. (2020). Promotion of Bacillus subtilis subsp. inaquosorum, Bacillus subtilis subsp. spizizenii and Bacillus subtilis subsp. stercoris to species status. *Antonie van Leeuwenhoek*, 113(1), 1-12.

[kma](https://doi.org/10.1186/s12859-018-2336-6) Clausen, P. T., Aarestrup, F. M., & Lund, O. (2018). Rapid and precise alignment of raw reads against redundant databases with KMA. *BMC bioinformatics*, 19(1), 1-8.

[deepMicrobes](https://doi.org/10.1093/nargab/lqaa009) Liang, Q., Bible, P. W., Liu, Y., Zou, B., & Wei, L. (2020). DeepMicrobes: taxonomic classification for metagenomics with deep learning. *NAR Genomics and Bioinformatics*, 2(1), lqaa009.

[clark](https://doi.org/10.1186/s12864-015-1419-2) Ounit, R., Wanamaker, S., Close, T. J., & Lonardi, S. (2015). CLARK: fast and accurate classification of metagenomic and genomic sequences using discriminative k-mers. *BMC genomics*, 16(1), 1-13.

[kraken2](https://doi.org/10.1186/s13059-019-1891-0) Wood, D. E., Lu, J., & Langmead, B. (2019). Improved metagenomic analysis with Kraken 2. *Genome biology*, 20(1), 1-13

inline:
Datta: [[1]](https://doi.org/10.1007/s10311-020-01010-z "Datta, S., Rajnish, K. N., Samuel, M. S., Pugazlendhi, A., & Selvarajan, E. (2020). Metagenomic applications in microbial diversity, bioremediation, pollution monitoring, enzyme and drug discovery. A review. *Environmental Chemistry Letters*, 18(4), 1229-1241.") 

Weizhong: [[2]](https://doi.org/10.1093/bib/bbs035 "Li, W., Fu, L., Niu, B., Wu, S., & Wooley, J. (2012). Ultrafast clustering algorithms for metagenomic sequence analysis. *Briefings in bioinformatics*, 13(6), 656-668.") 

ONT_lu: [[3]](https://doi.org/10.1016/j.gpb.2016.05.004 "Lu, H., Giordano, F., & Ning, Z. (2016). Oxford Nanopore MinION sequencing and genome assembly. *Genomics, proteomics & bioinformatics*, 14(5), 265-279.")

kraken2: [[4]](https://doi.org/10.1186/s13059-019-1891-0 "Wood, D. E., Lu, J., & Langmead, B. (2019). Improved metagenomic analysis with Kraken 2. *Genome biology*, 20(1), 1-13.") 

clark: [[5]](https://doi.org/10.1186/s12864-015-1419-2 "Ounit, R., Wanamaker, S., Close, T. J., & Lonardi, S. (2015). CLARK: fast and accurate classification of metagenomic and genomic sequences using discriminative k-mers. *BMC genomics*, 16(1), 1-13.") 

ccmetagen: [[6]](https://doi.org/10.1186/s13059-020-02014-2 "Marcelino, V. R., Clausen, P. T., Buchmann, J. P., Wille, M., Iredell, J. R., Meyer, W., ... & Holmes, E. C. (2020). CCMetagen: comprehensive and accurate identification of eukaryotes and prokaryotes in metagenomic data. *Genome biology*, 21, 1-15.") 

centrifuge: [[7]](https://doi.org/10.1101%2Fgr.210641.116 "Kim, D., Song, L., Breitwieser, F. P., & Salzberg, S. L. (2016). Centrifuge: rapid and sensitive classification of metagenomic sequences. *Genome research*, 26(12), 1721-1729.") 

kaiju: [[8]](https://doi.org/10.1186/s13062-018-0208-7 "Menzel, P., Ng, K. L., & Krogh, A. (2016). Fast and sensitive taxonomic classification for metagenomics with Kaiju. *Nature communications*, 7(1), 1-9.") 

diamond: [[9]](https://doi.org/10.1038/nmeth.3176 "Buchfink, B., Xie, C., & Huson, D. H. (2015). Fast and sensitive protein alignment using DIAMOND. *Nature methods*, 12(1), 59-60.") 

benchmark/1: [[10]](https://doi.org/10.1016/j.cell.2019.07.010 "Simon, H. Y., Siddle, K. J., Park, D. J., & Sabeti, P. C. (2019). Benchmarking metagenomics tools for taxonomic classification. *Cell*, 178(4), 779-794.")

morgan2012: [[11]](https://doi.org/10.1186/gb-2012-13-9-r79 "Morgan, X. C., Tickle, T. L., Sokol, H., Gevers, D., Devaney, K. L., Ward, D. V., ... & Huttenhower, C. (2012). Dysfunction of the intestinal microbiome in inflammatory bowel disease and treatment. *Genome Biology*, 13(9), 1-18.") 

zymoeven: [[12]](https://www.zymoresearch.de/collections/zymobiomics-microbial-community-standards/products/zymobiomics-microbial-community-standard "Zymo Research Corporation, Irvine, CA, USA. Product D6300, Lot ZRC190633") 

zymolog: [[13]](https://www.zymoresearch.de/collections/zymobiomics-microbial-community-standards/products/zymobiomics-microbial-community-standard-ii-log-distribution "Zymo Research Corporation, Irvine, CA, USA. Product D6310, Lot ZRC190842") 

datapaper: [[14]](https://doi.org/10.1093/gigascience/giz043 "Nicholls, S. M., Quick, J. C., Tang, S., & Loman, N. J. (2019). Ultra-deep, long-read nanopore sequencing of mock microbial community standards. *Gigascience*, 8(5), giz043.") 

kma: [[15]](https://doi.org/10.1186/s12859-018-2336-6 "Clausen, P. T., Aarestrup, F. M., & Lund, O. (2018). Rapid and precise alignment of raw reads against redundant databases with KMA. *BMC bioinformatics*, 19(1), 1-8.") 

conda: [[16]](https://docs.anaconda.com/ "Anaconda Software Distribution. (2020). Anaconda Documentation. *Anaconda Inc.* Retrieved from https://docs.anaconda.com/") 

snakemake: [[17]](https://snakemake.readthedocs.io/en/stable/ "Köster, J., & Rahmann, S. (2012). Snakemake—a scalable bioinformatics workflow engine. Bioinformatics, 28(19), 2520-2522.") 

blast: [[18]](https://doi.org/10.1016/S0022-2836(05)80360-2 "Altschul, S. F., Gish, W., Miller, W., Myers, E. W., & Lipman, D. J. (1990). Basic local alignment search tool. *Journal of molecular biology*, 215(3), 403-410.") 

PRROC: [[19]](https://cran.r-project.org/web/packages/PRROC/index.html "Jens Keilwagen, Ivo Grosse and Jan Grau (2014). Area under Precision-Recall Curves for Weighted and Unweighted Data. *PLOS ONE* (9) 3.") 
MLSTToxi: [[20]](https://www.sciencedirect.com/science/article/pii/S0580951715000148 "Dingle, T. C., & MacCannell, D. R. (2015). Molecular strain typing and characterisation of toxigenic Clostridium difficile. *Methods in Microbiology*, 42, 329-357.") 

PubMLST: [[21]](https://pubmlst.org/multilocus-sequence-typing "Public databases for molecular typing and microbial genome diversity. Multi-Locus Sequence Typing. Retrieved from https://pubmlst.org/multilocus-sequence-typing. Last visited on 21/04/2021.") 

MLSTfermentum: [[22]](https://doi.org/10.1007/s00203-017-1346-5 "Poluektova, E. U., Yunes, R. A., Epiphanova, M. V., Orlova, V. S., & Danilenko, V. N. (2017). The Lactobacillus rhamnosus and Lactobacillus fermentum strains from human biotopes characterized with MLST and toxin-antitoxin gene polymorphism. *Archives of microbiology*, 199(5), 683-690.") 

MLSTcryptococcus: [[23]](https://doi.org/10.1080/13693780902953886 "Meyer, W., Aanensen, D. M., Boekhout, T., Cogliati, M., Diaz, M. R., Esposto, M. C., ... & Kwon-Chung, J. (2009). Consensus multi-locus sequence typing scheme for Cryptococcus neoformans and Cryptococcus gattii. *Medical mycology*, 47(6), 561-570.") 

MLST_Saccharomyces: [[24]](https://doi.org/10.1007/s10068-018-0335-z "Eeom, Y. J., Son, S. Y., Jung, D. H., Hur, M. S., Kim, C. M., Park, S. Y., ... & Park, C. S. (2018). Diversity analysis of Saccharomyces cerevisiae isolated from natural sources by multilocus sequence typing (MLST). *Food science and biotechnology*, 27(4), 1119-1127.") 

bugSeq: [[25]](https://doi.org/10.1186/s12859-021-04089-5 "Fan, J., Huang, S., & Chorlton, S. D. (2021). BugSeq: a highly accurate cloud platform for long-read metagenomic analyses. *BMC bioinformatics*, 22(1), 1-12.") 

renamingFermentum: [[26]](https://doi.org/10.1099/ijsem.0.004107 "Zheng, J., Wittouck, S., Salvetti, E., Franz, C. M., Harris, H. M., Mattarelli, P., ... & Lebeer, S. (2020). A taxonomic note on the genus Lactobacillus: Description of 23 novel genera, emended description of the genus Lactobacillus Beijerinck 1901, and union of Lactobacillaceae and Leuconostocaceae. *International journal of systematic and evolutionary microbiology*, 70(4), 2782-2858.") 

subSpecB: [[27]](https://doi.org/10.1007/s10482-019-01354-9 "Dunlap, C. A., Bowman, M. J., & Zeigler, D. R. (2020). Promotion of Bacillus subtilis subsp. inaquosorum, Bacillus subtilis subsp. spizizenii and Bacillus subtilis subsp. stercoris to species status. *Antonie van Leeuwenhoek*, 113(1), 1-12.") 

NBC: [[28]](https://academic.oup.com/bioinformatics/article/27/1/127/202209 "Rosen, G. L., Reichenberger, E. R., & Rosenfeld, A. M. (2011). NBC: the Naive Bayes Classification tool webserver for taxonomic classification of metagenomic reads. *Bioinformatics*, 27(1), 127-129.") 

kslam: [[29]](https://academic.oup.com/nar/article/45/4/1649/2674183 "Ainsworth, D., Sternberg, M. J., Raczy, C., & Butcher, S. A. (2017). k-SLAM: accurate and ultra-fast taxonomic classification and gene identification for large metagenomic data sets. *Nucleic acids research*, 45(4), 1649-1656.")

lime: [[30]](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-020-03628-w "Guerrini, V., Louza, F. A., & Rosone, G. (2020). Metagenomic analysis through the extended Burrows-Wheeler transform. *BMC bioinformatics*, 21(8), 1-25.") 

taxmaps: [[31]](https://genome.cshlp.org/content/28/5/751 "Corvelo, A., Clarke, W. E., Robine, N., & Zody, M. C. (2018). taxMaps: comprehensive and highly accurate taxonomic classification of short-read data in reasonable time. *Genome research*, 28(5), 751-758.") 

metaothello: [[32]](https://doi.org/10.1093/bioinformatics/btx432 "Liu, X., Yu, Y., Liu, J., Elliott, C. F., Qian, C., & Liu, J. (2018). A novel data structure to support ultra-fast taxonomic classification of metagenomic sequences with k-mer signatures. *Bioinformatics*, 34(1), 171-178.") 

deepmicrobes: [[33]](https://doi.org/10.1093/nargab/lqaa009 "Liang, Q., Bible, P. W., Liu, Y., Zou, B., & Wei, L. (2020). DeepMicrobes: taxonomic classification for metagenomics with deep learning. *NAR Genomics and Bioinformatics*, 2(1), lqaa009.") 

[[34]](https://doi.org/10.1093/database/baaa062 "Schoch, C. L., Ciufo, S., Domrachev, M., Hotton, C. L., Kannan, S., Khovanskaya, R., ... & Karsch-Mizrachi, I. (2020). NCBI Taxonomy: a comprehensive update on curation, resources and tools. *Database*, 2020.") 