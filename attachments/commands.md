<!-- 
This file contains the commands used after the tools have been successfully installed. It contains downloading the mandatory databases, weights or indices.-->

# Tool-Specs

|     Tool     |   Version  |   Type  |         Approach        |                       Reference                      |   conda  |
|:------------:|:----------:|:-------:|:-----------------------:|:----------------------------------------------------:|:--------:|
|   Diamond    | 2.0.5     | Protein |        Alignment        | http://www.diamondsearch.org/index.php                |projectMAIN|
|     Kaiju    |    1.7.4   | Protein |   FM-Index, Alignment   |               http://kaiju.binf.ku.dk/               |projectMAIN|
|    BugSeq   |     beta???    |   DNA   |         Bayesian statistical framework        |          https://bugseq.com/free         | Cloud Service|
|   CCMetagen  |    1.2.3   |   DNA   |                         |       https://github.com/vrmarcelino/CCMetagen       |diamond|
|  Centrifuge  |    1.0.4   |   DNA   |         FM-Index        | https://ccb.jhu.edu/software/centrifuge/manual.shtml |classification|
|     CLARK    |    1.2.5   |   DNA   |      (spaced) k-mer     |           http://clark.cs.ucr.edu/Overview/          |projectMAIN|
|    Kraken2   | 2.0.7-beta |   DNA   |          k-mer          |         http://ccb.jhu.edu/software/kraken2/         |projectMAIN|
| DeepMicrobes |git rev. 43b654b  |DNA| Machine Learning, k-mer |      https://github.com/MicrobeLab/DeepMicrobes      ||
|    k-SLAM    |     1.0    |   DNA   |          k-mer          |            https://github.com/aindj/k-SLAM           ||
|  MetaOthello |git rev. 15ded5e  |DNA|          k-mer          |         https://github.com/xa6xa6/metaOthello        ||
| NBC           |           | DNA | |http://nbc.ece.drexel.edu/| Webserver |
|    taxMaps   |     0.2    |   DNA   |         FM-Index        |          https://github.com/nygenome/taxmaps         ||
|  LiMe | -  |DNA|          BW-Transform         |         https://github.com/veronicaguerrini/LiME        ||
|  MetaMaps | -  |DNA|          EM, Alignments          |         https://github.com/DiltheyLab/MetaMaps        ||
- conda 4.7.5, snakemake 3.10.0

# Tools: Installed
## Used
### Diamond
_Installation_

    conda install -c conda-forge boost-cpp=1.70.0
    conda install -c bioconda diamond=2.0.5

_Preparation_

    diamond makedb --in /mnt/fass1/genomes/new_bacteria/bacteria_blast_db/proteome/full_proteome_bacteria.faa -d nr --taxonmap /mnt/fass1/genomes/new_bacteria/bacteria_blast_db/prot_accession2taxid.txt --taxonnames names.dmp --taxonnodes nodes.dmp

### Kaiju
_Installation_

    conda install -c bioconda kaiju

_Preparation_   

    wget -P /mnt/fass1/kirsten "http://kaiju.binf.ku.dk/database/kaiju_db_refseq_2020-05-25.tgz"
    
    tar zxvf kaiju_db_refseq_2020-05-25.tgz

### BugSeq

    https://bugseq.com/free

### CCMetagen
_Installation_
    
    conda install -c etetoolkit ete3
    conda install -c bioconda ccmetagen

_Preparation_

    wget -P /mnt/fass1/kirsten/ccmetagen http://www.cbs.dtu.dk/public/CGE/databases/CCMetagen/ncbi_nt_kma.zip
    unzip ncbi_nt_kma

### Centrifuge
_Installation_

    not needed

_Preparation_

    wget https://genome-idx.s3.amazonaws.com/centrifuge/p_compressed_2018_4_15.tar.gz -O index.tar.gz


### CLARK
_Installation_

    conda install -c bioconda clark

_Preparation_
    ## README: /mnt/fass1/database/clark_database/README.sh
    # 07.12.2020
    # KL - set up DB for Jasmin
    /data/prostlocal2/projects/jb_chlamydomonasvirome_mittag/clark/CLARKSCV1.2.6.1/set_targets.sh /data/fass1/database/clark_db bacteria viruses

### Kraken2
_Installation_

    conda install -c bioconda/label/cf201901 kraken2

 _Preparation_
    Not needed, database already existent in /mnt/fass1/database/kraken2-database

## Not used
### DeepMicrobes
<!-- 
https://github.com/MicrobeLab/DeepMicrobes/blob/master/document/install.md-->
_Installation_

    git clone https://github.com/MicrobeLab/DeepMicrobes.git
    conda env create -f DeepMicrobes/install.yml
    conda activate DeepMicrobes

<!-- changed path to python in file!
/home/re85gih/miniconda3/envs/DeepMicrobes/bin/python
-->
_Preparation_
<!-- species weights-->
    wget -P /mnt/fass1/kirsten/deepMicrobes -O "weights_species.tar.gz" https://onedrive.gimhoy.com/sharepoint/aHR0cHM6Ly9tYWlsMnN5c3VlZHVjbi1teS5zaGFyZXBvaW50LmNvbS86dTovZy9wZXJzb25hbC9saWFuZ3F4N19tYWlsMl9zeXN1X2VkdV9jbi9FU0EtWnZwdVlqcEZqTHlkb2U2Tzl2OEJLOW5PbnFrdkdvOWpuaW56VGE5V0tnP2U9dGo2b3Vo.weights_species.tar.gz
    
    tar -xzvf weights_species.tar.gz
<!-- kmers-->
    wget -P /mnt/fass1/kirsten/deepMicrobes https://github.com/MicrobeLab/DeepMicrobes-data/raw/master/vocabulary/tokens_merged_12mers.txt.gz
    
    gunzip tokens_merged_12mers.txt.gz

<!-- exporting paths-->
    export PATH=/home/re85gih/projectClassification/DeepMicrobes/pipelines:$PATH
    export PATH=/home/re85gih/projectClassification/DeepMicrobes/scripts:$PATH
    export PATH=/home/re85gih/projectClassification/DeepMicrobes:$PATH
### k-SLAM
_Installation_

    conda install -c anaconda boost=1.64
    conda install -c bioconda k-slam

_Preparation_

    install_slam.sh /mnt/fass1/kirsten/kslam bacteria
### MetaOthello
_Installation_

    git clone https://github.com/xa6xa6/metaOthello/
    git clone https://github.com/gmarcais/Jellyfish.git

_Preparation_

    # k-mers
    https://drive.google.com/open?id=0BxgO-FKbbXRIa0Flc3Q4bWtycGM
    # species2tasID
    https://drive.google.com/open?id=0BxgO-FKbbXRIc3FkLVFvMlpVVGM
    # NCBI names
    https://drive.google.com/open?id=0BxgO-FKbbXRIUFI2dHlBMXZhdTA
### NBC
    http://nbc.ece.drexel.edu/newJob.php
### taxMaps
_Installation_

    conda create -n taxmaps python=2.7
    git clone git://github.com/nygenome/taxmaps.git
    pip install numpy==1.7
    conda install -c bioconda samtools
    conda install -c bioconda cutadapt
    conda install -c bioconda prinseq
    conda install -c bioconda gem3-mapper
    conda install -c bioconda krona
<!-- changed the path for python env in taxMaps-file into /home/re85gih/miniconda3/envs/taxmaps/bin/python2.7 -->

_Preparation_

<!--for Krona -->
    export PERL5LIB=/home/re85gih/miniconda3/envs/taxmaps/opt/krona/lib/
<!-- for usability-->
    export PATH=$PATH:/home/re85gih/projectClassification/taxmaps/

<!-- as of 06.03.18 -->
    wget -P /mnt/fass1/kirsten/taxmaps "ftp://ftp.nygenome.org/taxmaps/Indexes/refseq_complete_bacarchvir/*"
    
    wget -P /mnt/fass1/kirsten/taxmaps "ftp://ftp.nygenome.org/taxmaps/Indexes/taxonomy.tbl.gz"

## No installation possible
### LiME

    git clone https://github.com/veronicaguerrini/LiME
    cd LiME
    make EBWT=0

### MetaMaps

    conda install -c bioconda metamaps 
    # and several required updates