<!-- This file contains the commands used after the tools have been successfully installed. It contains downloading the mandatory databases, weights or indices.-->

# Tool-Version Table
- Kaiju 1.7.4
- Kraken version 2.0.7-beta
- Centrifuge
- taxMaps v0.2
- DeepMicrobes
- MetaOthello
- k-SLAM 1.0
- CLARK Version: 1.2.5
- CCMetagen v1.2.3
# Tools
## Kaiju
<!-- conda install -c bioconda kaiju in projectMAIN -->
    wget -P /mnt/fass1/kirsten "http://kaiju.binf.ku.dk/database/kaiju_db_refseq_2020-05-25.tgz"

## taxMaps
<!-- 
conda create -n taxmaps python=2.7
git clone git://github.com/nygenome/taxmaps.git
pip install numpy==1.7
conda install -c bioconda samtools
conda install -c bioconda cutadapt
conda install -c bioconda prinseq
conda install -c bioconda gem3-mapper
conda install -c bioconda krona
-->

<!-- changed the path for python env in taxMaps-file into /home/re85gih/miniconda3/envs/taxmaps/bin/python2.7 -->
  
<!--for Krona -->
    export PERL5LIB=/home/re85gih/miniconda3/envs/taxmaps/opt/krona/lib/
<!-- for usability-->
    export PATH=$PATH:/home/re85gih/projectClassification/taxmaps/

<!-- Stand der Downloads: 06.03.18 -->
    wget -P /mnt/fass1/kirsten/taxmaps "ftp://ftp.nygenome.org/taxmaps/Indexes/refseq_complete_bacarchvir/*"
    wget -P /mnt/fass1/kirsten/taxmaps "ftp://ftp.nygenome.org/taxmaps/Indexes/taxonomy.tbl.gz"

## DeepMicrobes
<!-- 
https://github.com/MicrobeLab/DeepMicrobes/blob/master/document/install.md

git clone https://github.com/MicrobeLab/DeepMicrobes.git
conda env create -f DeepMicrobes/install.yml
conda activate DeepMicrobes

changed path to python in file!
/home/re85gih/miniconda3/envs/DeepMicrobes/bin/python
-->
    wget -P /mnt/fass1/kirsten/deepMicrobes -O "weights_species.tar.gz" https://onedrive.gimhoy.com/sharepoint/aHR0cHM6Ly9tYWlsMnN5c3VlZHVjbi1teS5zaGFyZXBvaW50LmNvbS86dTovZy9wZXJzb25hbC9saWFuZ3F4N19tYWlsMl9zeXN1X2VkdV9jbi9FU0EtWnZwdVlqcEZqTHlkb2U2Tzl2OEJLOW5PbnFrdkdvOWpuaW56VGE5V0tnP2U9dGo2b3Vo.weights_species.tar.gz
    
    tar -xzvf weights_species.tar.gz
    
    wget -P /mnt/fass1/kirsten/deepMicrobes https://github.com/MicrobeLab/DeepMicrobes-data/raw/master/vocabulary/tokens_merged_12mers.txt.gz
    
    gunzip tokens_merged_12mers.txt.gz

    export PATH=/home/re85gih/projectClassification/DeepMicrobes/pipelines:$PATH
    export PATH=/home/re85gih/projectClassification/DeepMicrobes/scripts:$PATH
    export PATH=/home/re85gih/projectClassification/DeepMicrobes:$PATH

## k-SLAM
    install_slam.sh /mnt/fass1/kirsten/kslam bacteria

### CLARK
    set_targets.sh /mnt/fass1/kirsten/clark /mnt/fass1/kirsten/kslam/bacteria
<!-- Geht so nicht, weil das keine fasta-Files in bacteria sind?-->

## CCMetagen
    wget -P /mnt/fass1/kirsten/ccmetagen http://www.cbs.dtu.dk/public/CGE/databases/CCMetagen/ncbi_nt_kma.zip
    unzip ncbi_nt_kma

