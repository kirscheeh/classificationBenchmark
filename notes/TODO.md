### note ccmetagen 366: mapped:80.737475%

# TODO LIST
- install Jellyfish for MetaOthello

- more information on benchmarking
  - leave one taxa out approach aka clade exclusion
  - existing benchmarking datasets
  - --> they did three things: clade exclusion, high-complexity fold standard CAMI assembly and recently publisehd sequences


- centrifuge
  - no difference if w/ or w/o -ignore-quals 

# Table AUPR, ASP
| sample     	| tool       	| AUPR   	| baseline 	| ASP     	|
|------------	|------------	|--------	|----------	|---------	|
| gridion364 	| centrifuge 	| 0.7981 	| 0.0036   	| 0.01679 	|
| gridion364 	| kraken2    	| 0.9979 	| 0.00256  	| 0.01794 	|
| gridion364 	| kaiju      	| 0.4728 	| 0.00247  	| 0.05179 	|

# Table Abundancies
| sample, tool | Bacillus subtilis | Listeria monocytogenes | Enterococcus faecalis | Staphylococcus aureus | Salmonella enterica | Escherichia coli | Pseudomonas aeruginosa | Lactobacillus fermentum | Saccharomyces cerevisiae | Cryptococcus neoformans |
|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|---|
|truth|0.12|0.12|0.12|0.12|0.12|0.12|0.12|0.12|0.02|0.02|
| gridion364, kraken2 | 0.17514371067110807| 0.128698598552439| 0.11110932894921507| 0.11066767104219237| 0.05685214198356529| 0.05254612059953199| 0.04480679614709328| 0.14142218428763328| 0.021756091413448513| 0.020032995454532434|
|gridion364, kaiju|0.008112241829185511| 0.09322046520153864| 0.10269090534142562| 0.04151326549024887| 0.017789189978776362| 0.02124483371952145| 0.011038583486806114| 0.1250292863300863|
|gridion364, centrifuge| 0.18033222980001143| 0.13268354876744617| 0.10978380289037058| 0.11039120082853578| 0.05890522708106204| 0.05824580663430398| 0.05114965525948968| 0.14248487058908882|
|gridion366, kraken2|0.010274629991165596| 0.8129274051937571| 0.0016234580693009913| 3.790068384831001e-05| 0.00048289288557810814| 0.0004796208840948008| 0.03980280737727268| 5.1534023362090594e-05| 0.006906649797681241| 2.699401223728555e-05|


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

## metaothello
segmentation fraud

## catbat
- seems to need contigs, not just long metagenomic sequences



