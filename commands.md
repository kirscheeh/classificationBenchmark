<!-- This file contains the commands used after the tools have been successfully installed. It contains downloading the mandatory databases, weights or indices.-->

# Tool-Versions and Conda-Environment
- Kaiju 1.7.4 --> projectMAIN
- Kraken version 2.0.7-beta--> projectMAIN
- Centrifuge version 1.0.4 --> classification
- taxMaps v0.2 --> taxmaps
- DeepMicrobes --> DeepMicrobes
- MetaOthello --> projectMAIN
- k-SLAM 1.0 --> kslam
- CLARK Version: 1.2.5 --> projectMAIN
- CCMetagen v1.2.3 --> projectMAIN
# Tools
## Kaiju
_Installation_

    conda install -c bioconda kaiju in projectMAIN

_Preparation_   

    wget -P /mnt/fass1/kirsten "http://kaiju.binf.ku.dk/database/kaiju_db_refseq_2020-05-25.tgz"
    
    tar zxvf kaiju_db_refseq_2020-05-25.tgz

## taxMaps
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

<!-- Stand der Downloads: 06.03.18 -->
    wget -P /mnt/fass1/kirsten/taxmaps "ftp://ftp.nygenome.org/taxmaps/Indexes/refseq_complete_bacarchvir/*"
    
    wget -P /mnt/fass1/kirsten/taxmaps "ftp://ftp.nygenome.org/taxmaps/Indexes/taxonomy.tbl.gz"

## DeepMicrobes
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

## k-SLAM
_Installation_

    conda install -c bioconda k-slam

_Preparation_

    install_slam.sh /mnt/fass1/kirsten/kslam bacteria

### CLARK
_Installation_

    conda install -c bioconda clark

_Preparation_

    set_targets.sh /mnt/fass1/kirsten/clark /mnt/fass1/kirsten/kslam/bacteria
<!-- Geht so nicht, weil das keine fasta-Files in bacteria sind?-->

## CCMetagen
_Installation_

    conda install -c bioconda ccmetagen

_Preparation_

    wget -P /mnt/fass1/kirsten/ccmetagen http://www.cbs.dtu.dk/public/CGE/databases/CCMetagen/ncbi_nt_kma.zip
    unzip ncbi_nt_kma

## NBC
    http://nbc.ece.drexel.edu/newJob.php

## Kraken2
_Installation_

    conda install -c bioconda/label/cf201901 kraken2

## MetaOthello
_Installation_

    git clone https://github.com/xa6xa6/metaOthello/

_Preparation_

    Scheitert am Viren-Schutz von Google-Drive
