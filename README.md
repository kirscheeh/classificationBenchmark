# Project Module / Master Thesis

Benchmarking different classification tools for the usability on long reads.

## Tools
|     Tool     |   Version  |   Type  |         Approach        |                       Reference                      |
|:------------:|:----------:|:-------:|:-----------------------:|:----------------------------------------------------:|
|     Kaiju    |    1.7.4   | Protein |   FM-Index, Alignment   |               http://kaiju.binf.ku.dk/               |
|    Kraken2   | 2.0.7-beta |   DNA   |          k-mer          |         http://ccb.jhu.edu/software/kraken2/         |
|  Centrifuge  |    1.0.4   |   DNA   |         FM-Index        | https://ccb.jhu.edu/software/centrifuge/manual.shtml |
|    taxMaps   |     0.2    |   DNA   |         FM-Index        |          https://github.com/nygenome/taxmaps         |
| DeepMicrobes |            |   DNA   | Machine Learning, k-mer |      https://github.com/MicrobeLab/DeepMicrobes      |
|  MetaOthello |            |   DNA   |          k-mer          |         https://github.com/xa6xa6/metaOthello        |
|    k-SLAM    |     1.0    |   DNA   |          k-mer          |            https://github.com/aindj/k-SLAM           |
|     CLARK    |    1.2.5   |   DNA   |      (spaced) k-mer     |           http://clark.cs.ucr.edu/Overview/          |
|   CCMetagen  |    1.2.3   |   DNA   |                         |       https://github.com/vrmarcelino/CCMetagen       |
|      NCB     |            |   DNA   |                         |               http://nbc.ece.drexel.edu/             |

## Metrics
- AUPR
- Abundace Profile Similarity
- Runtime, Database Size, Memory, ...


