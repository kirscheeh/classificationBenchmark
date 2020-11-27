<!-- This file contains the commands used after the tools have been successfully installed. It contains downloading the mandatory databases, weights or indices.-->

# Tool-Version Table
- Kaiju 1.7.4
- diamond version 0.9.14
# Tools
## taxMaps
- changed the path for python env in taxMaps into /home/re85gih/miniconda3/envs/taxmaps/bin/python2.7
- for Krona
    export PERL5LIB=/home/re85gih/miniconda3/envs/taxmaps/opt/krona/lib/

    export PATH=$PATH:/home/re85gih/projectClassification/taxmaps/

- still to do: numpy 1.7 für python2.7 herunterladen
- Stand der Downloads: 06.03.18
    wget -P /mnt/fass1/kirsten/taxmaps "ftp://ftp.nygenome.org/taxmaps/Indexes/refseq_complete_bacarchvir/*"
    wget -P /mnt/fass1/kirsten/taxmaps "ftp://ftp.nygenome.org/taxmaps/Indexes/taxonomy.tbl.gz"
## Kaiju
    wget -P /mnt/fass1/kirsten "http://kaiju.binf.ku.dk/database/kaiju_db_refseq_2020-05-25.tgz"

## Diamond

## DeepMicrobes
    wget -P /mnt/fass1/kirsten/deepMicrobes -O "weights_species.tar.gz" https://onedrive.gimhoy.com/sharepoint/aHR0cHM6Ly9tYWlsMnN5c3VlZHVjbi1teS5zaGFyZXBvaW50LmNvbS86dTovZy9wZXJzb25hbC9saWFuZ3F4N19tYWlsMl9zeXN1X2VkdV9jbi9FU0EtWnZwdVlqcEZqTHlkb2U2Tzl2OEJLOW5PbnFrdkdvOWpuaW56VGE5V0tnP2U9dGo2b3Vo.weights_species.tar.gz
    tar -xzvf weights_species.tar.gz
    wget -P /mnt/fass1/kirsten/deepMicrobes https://github.com/MicrobeLab/DeepMicrobes-data/raw/master/vocabulary/tokens_merged_12mers.txt.gz
    gunzip tokens_merged_12mers.txt.gz

    export PATH=/home/re85gih/projectClassification/DeepMicrobes/pipelines:$PATH
    export PATH=/home/re85gih/projectClassification/DeepMicrobes/scripts:$PATH
    export PATH=/home/re85gih/projectClassification/DeepMicrobes:$PATH

## k-SLAM
    install_slam.sh /mnt/fass1/kirsten/kslam bacteria viruses

### clark braucht auch refseq bacteria, die kann ich ja dann mit kslam vereinen http://clark.cs.ucr.edu/Overview/

