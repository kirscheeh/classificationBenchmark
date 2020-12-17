# Snakefile for project work of benchmarking different classification tools regarding their usability for long reads

configfile: "projectmaster/config.yaml"

rule create:
    shell:
        'python structure.py'

rule all:
    pass

rule centrifuge:
    input:
        pass
    output:
        pass
    benchmark:
        pass #repeat("benchmarks/{sample}.bwa.benchmark.txt", 3 für 3 runs
    log:
        pass #log folder?
    conda:
        '/home/re85gih/projectClassification/projectmaster/envs/centrifuge.yml'
    shell:
        # -q 				files are fastq
    	# -x 				index files
    	# --report-file 	generated report file
    	# -S 				output file
        # -f                query input files are (multi)fasta
        'centrifuge (-q|-f) -x INDEX_FILE {input} --report-file LOCATION_OF_REPORT -S {output}'

rule kraken2:
    input:
        pass 
    output:
        pass 
    conda:
        '/home/re85gih/projectClassification/projectmaster/envs/main.yml'
    shell:
        # --confidence          threshold that must be in [0,1]
        # --unclassified-out    prints unclassified sequences to filename
        # --classified-out      prints classified sequences to filename
        # --output              prints output to filename
        # --report              prints report with aggregate counts/clade to file
        'kraken2 (--confidence X) --db /mnt/fass1/database/kraken2-database --unclassified-out FILENAME_UN (--classified-out FILENAME_C) --report REPORT_NAME --output {output} {input}'

rule kaiju:
    input:
        pass 
    output:
        pass 
    conda:
        '/home/re85gih/projectClassification/projectmaster/envs/main.yml'
    shell:
        # -t    name of nodes.dmp file
        # -f    name of database (.fmi) file
        # -i    input file containing fasta/fastq
        # -o    name of output file
        # -m    minimum match length (default: 11)
        # -E    minimum e-value in Greedy mode (which is default)
        'kaiju -t /mnt/fass1/kirsten/kaiju/nodes.dmp -f /mnt/fass1/kirsten/kaiju/kaiju_db_refseq.fmi -i {input} -o {output} -m INT -E FLOAT'

rule taxmaps:
    input:
        pass 
    output:
        pass 
    conda:
        '/home/re85gih/projectClassification/projectmaster/envs/taxmaps.yml'
    shell:
        # -f        input fastq
        # -l        in preprocessing: minimum read length for mapping
        # -C        in preprocessing: entropy cutoff for low complexity filtering
        # -d        index files
        # -t        taxonomic rable
        # --cov     coverage histogram
        # -o        output directory
        'taxMaps -f {input} (-l INT -C INT) (--phred64) -t /mnt/fass1/kirsten/taxmaps/taxonomy.tbl.gz -d /mnt/fass1/kirsten/taxmaps/*.gem.* (--cov) -o {output}'

rule deepmicrobes: #this is goign to be fun...
    input:
        pass 
    output:
        pass 
    conda:
        '/home/re85gih/projectClassification/projectmaster/envs/deepmicrobes.yml'
    shell:
        # --kmer        length of k-mers (default: 12) --> if i want to change that i might need to build my own index
        # --max_lem     max length of sequences (default: 150)
        # --pred_out    path to prediction output
        # -dd           location of input data
        # -ebe          number of training epochs to run between evaluations
        
        # transform training fastq to tfrec
        'tfrec_train_kmer.sh -i train.fa -v /path/to/vocab/tokens_merged_12mers.txt -o train.tfrec -s 20480000 -k 12'
        # transform predicion fastq to tfrec
        'tfrec_predict_kmer.sh -f sample_R1.fastq -r sample_R2.fastq -t fastq -v /path/to/vocab/tokens_merged_12mers.txt -o sample_name -s 4000000 -k 12'
        # make prediction on metagenome datasaet
        'predict_DeepMicrobes.sh -i sample.tfrec -b 8192 -l species -p 8 -m model_dir -o prefix' 
        # generate taxonomic profiles
        'report_profile.sh -i predict.result.txt -o summarize.profile.txt -t 50 -l /path/to/DeepMicrobes/data/name2label.txt' 

rule kslam:
    input:
        database='/mnt/fass1/kirsten/kslam/database' 
    output:
        pass 
    conda:
        '/home/re85gih/projectClassification/projectmaster/envs/kslam.yml'
    shell:
        # --db                      database file
        # --min-alignment-score     alignment score cutoff
        'SLAM --db {databse} (--min-alignment-score INT) --output-file {output} {input}'

rule clark:
    input:
        pass 
    output:
        pass 
    conda:
        '/home/re85gih/projectClassification/projectmaster/envs/main.yml'
    shell:
        # -k        k-mer size, has to be between 2 and 32, default:31 
        # --long    for long reads (only for full mode)
        # -m        mode of execution
        'CLARK -k INT (--long) -m 0 -O {input} -R {output} -D {databse}'

rule ccmetagen: 
    input:
        pass 
    output:
        pass 
    conda:
        '/home/re85gih/projectClassification/projectmaster/envs/main.yml'
    shell:
        # -m    mode
        # -r    reference database
        # -i    path to kma result
        # -ef   extended output file that includes percentage of classified reads
        # -c    minimum coverage
        'CCMetagen.py  -o {output} -r RefSeq -i {database} -ef y -c INT'

rule catbat:
    input:
        pass
    output:
        pass
    conda:
        '/home/re85gih/projectClassification/projectmaster/envs/catbat.yml'
    shell:
        'CAT contigs -c {input} -d {databse} -t {taxonomy} -o {output}',
        'CAT bins -b {input} -d {database} -t {taxonomy} -o {output}',
        'CAT add_names -i {ORF2LCA / classification file} -o {output file} -t {taxonomy folder} --only_official'

rule diamond:
    input:
        pass
    output:
        pass 
    conda:
        '/home/re85gih/projectClassification/projectmaster/envs/main.yml'
    shell:
        'diamond blastx --db {database} -g {input} --taxonlist {database_list} -o {output}' #there are options for hit length, kinda?

rule metaothello:
    input:
        pass
    output:
        pass 
    conda:
        '/home/re85gih/projectClassification/projectmaster/envs/main.yml'
    shell:
        classifier {index} {output} 31 THREADS FA/FQ SE/PE spec2tax ncbiNames {input}