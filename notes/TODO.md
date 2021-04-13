### note ccmetagen 366: mapped:80.737475%

# TODO LIST

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
