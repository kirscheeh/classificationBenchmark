# TODO LIST
- create a structure so that all is reproducible
- script for seed length
- protocol

- more information on benchmarking
  - leave one taxa out approach aka clade exclusion
  - existing benchmarking datasets
  - --> they did three things: clade exclusion, high-complexity fold standard CAMI assembly and recently publisehd sequences

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



