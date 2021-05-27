|     Tool     |   Version      |   Type  |         Approach        |Default Database|Creation Date | Reference                                |
|:------------:|:----------:    |:-------:|:-----------------------:|:--------------:|:----------:   |:-----------------------------            |
|   Diamond    |    2.0.5       | Protein |        Alignment        | full proteome  |  27/07/2019  |http://www.diamondsearch.org/index.php    |
|     Kaiju    |    1.7.4       | Protein |   FM-Index, Alignment   |RefSeq          | 25/05/2020   |   http://kaiju.binf.ku.dk/               |
|   CCMetagen  |    1.2.3       |   DNA   |*k*-mer, Alignment (KMA) | NCBI nt        | 08/05/2019   | https://github.com/vrmarcelino/CCMetagen |
|  Centrifuge  |    1.0.4       |   DNA   |         FM-Index        | RefSeq         | 15/04/2018   |https://ccb.jhu.edu/software/centrifuge/manual.shtml |
|     CLARK    |    1.2.5       |   DNA   |       *k*-mer           | RefSeq         | 07/12/2020   |http://CLARK.cs.ucr.edu/Overview/          |
|    Kraken2   | 2.0.7-beta     |   DNA   |          *k*-mer        |-               |2019/2020|http://ccb.jhu.edu/software/kraken2/         |
|BugSeq        | v1             |  DNA    | Pipeline                | RefSeq               |-|https://bugseq.com/free |

***Table 3: Overview of Used Classification Tools and General Information.*** The creation dates are based on the date the donwloaded databases or indices are generated. For Kraken2, no exact can be given, since the [files](../paths.md "Line 11, 'Kraken2 Default Database'") have different creation or alteration dates. For BugSeq, no date can be given either. The database was generated 23/02/2020 and since then, updated each month [[25]](https://doi.org/10.1186/s12859-021-04089-5 "Fan, J., Huang, S., & Chorlton, S. D. (2021). BugSeq: a highly accurate cloud platform for long-read metagenomic analyses. *BMC bioinformatics*, 22(1), 1-12.").