# Kraken 2
conda install -c bioconda/label/cf201901 kraken2

# DeepMicrobes
https://github.com/MicrobeLab/DeepMicrobes/blob/master/document/install.md

git clone https://github.com/MicrobeLab/DeepMicrobes.git
conda env create -f DeepMicrobes/install.yml
conda activate DeepMicrobes <!-- DONE -->
<!-- pre-trained weights for species model-->
<!-- hab ich noch nicht heruntergeladen-->
wget -O "weights_species.tar.gz" https://onedrive.gimhoy.com/sharepoint/aHR0cHM6Ly9tYWlsMnN5c3VlZHVjbi1teS5zaGFyZXBvaW50LmNvbS86dTovZy9wZXJzb25hbC9saWFuZ3F4N19tYWlsMl9zeXN1X2VkdV9jbi9FU0EtWnZwdVlqcEZqTHlkb2U2Tzl2OEJLOW5PbnFrdkdvOWpuaW56VGE5V0tnP2U9dGo2b3Vo.weights_species.tar.gz
tar -xzvf weights_species.tar.gz
<!-- 12-mer vocabulary files-->
wget https://github.com/MicrobeLab/DeepMicrobes-data/raw/master/vocabulary/tokens_merged_12mers.txt.gz
gunzip tokens_merged_12mers.txt.gz
<!-- okay, was?-->
export PATH=/path/to/DeepMicrobes/pipelines:$PATH
export PATH=/path/to/DeepMicrobes/scripts:$PATH
export PATH=/path/to/DeepMicrobes:$PATH

# Lime ???
git clone https://github.com/veronicaguerrini/LiME
cd LiME
<!-- one of the follwing two make thingys; they are for different approaches-->
make <!-- chose this one-->
make EBWT=0

Install_Preprocessing_Tools.sh ging nicht (permission denied). Habs händisch versucht, Fehler bei egsa make; dont know why

# CCMetagen
https://github.com/vrmarcelino/CCMetagen

# Kaiju
conda install -c bioconda kaiju

# taxMaps
https://github.com/nygenome/taxmaps

conda create -n taxmaps python=2.7
pip install numpy==1.7
conda install -c bioconda samtools
conda install -c bioconda cutadapt
conda install -c bioconda prinseq
conda install -c bioconda gem3-mapper
conda install -c bioconda krona

# MetaOthello
https://github.com/xa6xa6/metaOthello/
--> kmere haben 26GB oder so

# k-SLAM
- kann BOOST nicht installieren

# Megan
conda install -c bioconda megan --> ich versteh nicht, warum er das tool nicht findet




