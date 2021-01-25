# Snakefile for project work of benchmarking different classification tools regarding their usability for long reads

configfile: "config.yaml"

DI= dict(config["dataIndex"])
PATH = config["path"]
SAMPLES = "gridion364 gridion366".split(" ")#list(config["samples"])
TOOLS= 'diamond centrifuge kraken2 kaiju'.split(" ")#list(config["classification"])
RUNS='default'# medium restrictive'.split()

rule all:
    input:
       expand("{path}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.classification", run=RUNS, sample=SAMPLES, tool=TOOLS, path=PATH),
       expand("{path}/result/classification/centrifuge/{run}/{sample}_{run}.centrifuge.kreport", run=RUNS, sample=SAMPLES, path=PATH),
      # expand("{path}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.classification", run=RUNS, sample=SAMPLES, tool=TOOLS, path=PATH)
# creating the project structure
rule create:
    shell:
        'python structure.py'

def get_run(wildcards): #returns the current value of variable/wildcard run
    return wildcards.run

#rule plot_readlength:
#    input:
#        fastq = "{PATH}/data/{sample}.fastq",
#        script = "{PATH}/result/classificationBenchmark/scripts/plotReadlength.py"
#    output:
 #       plot = "{PATH}/result/stats/{sample}_readlength.png"
 #   threads: 8
#    conda:
 #       "{PATH}/result/classificationBenchmark/envs/centrifuge.yaml"
 #   shell:
#        "python {input.script} {input.fastq} {output.plot}""""

rule centrifuge:
    input: 
        fastq = "{PATH}/data/{sample}.fastq"
    output:
        files = "{PATH}/result/classification/centrifuge/{run}/{sample}_{run}.centrifuge.classification",
        report= "{PATH}/result/classification/centrifuge/{run}/{sample}_{run}.centrifuge.report"
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.centrifuge.benchmark.txt"
        # repeat() #repeat("benchmarks/{sample}.bwa.benchmark.txt", 3 für 3 runs
    threads: 8
    params:
        runid=get_run,
	db = DI["centrifuge"]+"/p_compressed"
    log:
        "{PATH}/result/classification/centrifuge/{run}/{sample}_{run}.centrifuge.log"
    conda:
       "{PATH}/result/classificationBenchmark/envs/centrifuge.yaml"
    run:
        # -q 				files are fastq
    	# -x 				index files
    	# --report-file 	generated report file
    	# -S 				output file
        # -f                query input files are (multi)fasta
        # --ignore-quals
        
        if 'default' in {params.runid}:
            shell('centrifuge -q -x {params.db} {input.fastq} --report-file {output.report} -S {output.files}')
        elif 'medium' in {params.runid}: 
            print("Sure")
        elif 'restrictive' in {params.runid}: 
            print("Sure")
        else:
            print("Centrifuge -- Nothing to be done here:", {params.runid})

rule kreport:
    input:
        report="{PATH}/result/classification/centrifuge/{run}/{sample}_{run}.centrifuge.report"
    output:
        "{PATH}/result/classification/centrifuge/{run}/{sample}_{run}.centrifuge.kreport"
    conda:
       "{PATH}/result/classificationBenchmark/envs/centrifuge.yaml"
    params:
        db = DI["centrifuge"]+"/p_compressed"
    log: 
        "{PATH}/result/classification/centrifuge/{run}/{sample}_{run}.centrifuge.kreport"
    shell:
        'centrifuge-kreport -x {params.db} {input.report} > {log}'


rule kraken2:
    input:
        db = DI['kraken2'],
        files = "{PATH}/data/{sample}.fastq"
    output:
        files = "{PATH}/result/classification/kraken2/{run}/{sample}_{run}.kraken2.classification",
        report= '{PATH}/result/classification/kraken2/{run}/{sample}_{run}.kraken2.report',
        unclassified='{PATH}/result/classification/kraken2/{run}/{sample}_{run}.kraken2.unclassified'
    benchmark:
        '{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.kraken2.benchmark.txt'
    threads: 8
    params:
        runid=get_run
    log:
        '{PATH}/result/classification/kraken2/{run}/{sample}_{run}.kraken2.log'
    conda:
        '{PATH}/result/classificationBenchmark/envs/main.yaml'
    run:
        # --confidence          threshold that must be in [0,1]
        # --unclassified-out    prints unclassified sequences to filename
        # --classified-out      prints classified sequences to filename
        # --output              prints output to filename
        # --report              prints report with aggregate counts/clade to file
        
        if 'default' in {params.runid}:
            shell('kraken2 --db {input.db} --unclassified-out {output.unclassified} --report {output.report} --threads {threads} --output {output.files} {input.files}')
        elif 'medium' in {params.runid}: 
            print("Indeed")
        elif 'restrictive' in {params.runid}: 
            print("Sure") 
        else:
            print("Kraken2 -- Nothing to do here:", {params.runid})           

rule kaiju:
    input:
        db = DI['kaiju']+"/kaiju_db_refseq.fmi",
        nodes = DI['kaiju']+"/nodes.dmp",
        files = "{PATH}/data/{sample}.fastq"
    output:
        files = '{PATH}/result/classification/kaiju/{run}/{sample}_{run}.kaiju.classification'
    benchmark:
        '{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.kaiju.benchmark.txt'
    threads: 8
    params:
        runid=get_run
    log:
        '{PATH}/result/classification/kaiju/{run}/{sample}_{run}.kaiju.log'
    conda:
        '{PATH}/result/classificationBenchmark/envs/main.yaml'
    run:
        # -t    name of nodes.dmp file
        # -f    name of database (.fmi) file
        # -i    input file containing fasta/fastq
        # -o    name of output filetax  
        # -m    minimum match length (default: 11)
        # -E    minimum e-value in Greedy mode (which is default)
        if 'default' in {params.runid}:
            shell('kaiju -t {input.nodes} -f {input.db} -i {input.files} -o {output.files} -z {threads} -v')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass
        else:
            print("Kaiju -- Nothing to do here:", {params.runid})


rule taxmaps:
    input:
        db = DI['taxmaps']+"/*.gem.*",
        taxonomy = DI['taxmaps']+"/taxonomy.tbl.gz",
        nodes = DI['kaiju']+"/nodes.dmp",
        files = "{PATH}/data/{sample}.fastq.gz"
    benchmark:
        '{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.taxmaps.benchmark.txt'
    output:
        files = '{PATH}/result/classification/taxmaps/{run}/{sample}_{run}.taxmaps.classification' 
    threads: 8
    params:
        runid=get_run
    log:
        '{PATH}/result/classification/taxmaps/{run}/{sample}_{run}.taxmaps.log'
    conda:
        '{PATH}/result/classificationBenchmark/envs/taxmaps.yaml'
    run:
        # -f        input fastq
        # -l        in preprocessing: minimum read length for mapping
        # -C        in preprocessing: entropy cutoff for low complexity filtering
        # -d        index files
        # -t        taxonomic rable
        # --cov     coverage histogram
        # -o        output directory
        if 'default' in {params.runid}:
            shell('taxMaps -f {input.files} (--phred64) -t {input.taxonomy} -d {input.db} -o {output.files}')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass   
        else:
            print("TaxMaps -- Nothing to do here:", {params.runid}) 

"""rule deepmicrobes: #this is goign to be fun...
    input:
        pass 
    output:
        pass 
    conda:
        '{PATH}/result/classificationBenchmark/envs/deepmicrobes.yaml'
    shell:
        # --kmer        length of k-mers (default: 12) --> if i want to change that i might need to build my own index
        # --max_len     max length of sequences (default: 150)
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
        'report_profile.sh -i predict.result.txt -o summarize.profile.txt -t 50 -l /path/to/DeepMicrobes/data/name2label.txt'"""

rule kslam:
    input:
        db = DI['kslam'],
        files = "{PATH}/data/{sample}.fastq"
    output:
        files = '{PATH}/result/classification/kslam/{run}/{sample}_{run}.kslam.classification' 
    benchmark:
        '{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.kslam.benchmark.txt'
    threads: 8
    params:
        runid=get_run
    log:
        '{PATH}/result/classification/kslam/{run}/{sample}_{run}.kslam.log'
    conda:
        '{PATH}/result/classificationBenchmark/envs/kslam.yaml'
    run:
        # --db                      database file
        # --min-alignment-score     alignment score cutoff
        if 'default' in {params.runid}:
            shell('SLAM --db {input.db} --output-file {output} {input.files}')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass
        else:
            print("KSLAM -- Nothing to do here:", {params.runid})
        
rule clark:
    input:
        db = DI['clark'],
        files = "{PATH}/data/{sample}.fastq"
    output:
        files = '{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification' 
    benchmark:
        '{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.clark.benchmark.txt'
    threads: 8
    params:
	    runid=get_run
    log:
        '{PATH}/result/classification/kslam/{run}/{sample}_{run}.clark.log'
    conda:
        '{PATH}/result/classificationBenchmark/envs/main.yaml'
    run:
        # -k        k-mer size, has to be between 2 and 32, default:31 
        # --long    for long reads (only for full mode)
        # -m        mode of execution

        if 'default' in {params.runid}:
            shell('CLARK --long -O {input.files} -R {output} -D {input.db} -n {threads}')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass
        else:
            print("CLARK -- Nothing to do here:", {params.runid})

rule kma:
    input:
        db = DI['ccmetagen'],
        files = "{PATH}/data/{sample}.fastq.gz"
    output:
        '{PATH}/result/classification/ccmetagen/{sample}.kma.intermediate'
    benchmark:
        '{PATH}/result/classification/benchmarks/{sample}.kma.benchmark.txt'
    threads: 8
    log:
        '{PATH}/result/classification/ccmetagen/{sample}.kma.log'
    conda:
        '{PATH}/result/classificationBenchmark/envs/main.yaml'
    run:
        'kma -i {input.files} -t_db {input.db} -o {output} -t {threads} -1t1 -mem_mode -and -ef'

rule ccmetagen: 
    input:
        kma = DI['ccmetagen']+"/{sample}.kma.intermediate",
        files = "{PATH}/data/{sample}.fastq.gz"
    output:
        files = '{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.classification',
        report= '{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.report'
    benchmark:
        '{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.ccmetagen.benchmark.txt'
    threads: 8
    params:
	    runid=get_run
    log:
        '{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.log'
    conda:
        '{PATH}/result/classificationBenchmark/envs/main.yaml'
    run:
        # -m    mode
        # -r    reference database
        # -i    path to kma result
        # -ef   extended output file that includes percentage of classified reads
        # -c    minimum coverage
        if 'default' in {params.runid}:
            shell('CCMetagen.py  -o {output.files} -i {input.kma} -ef {output.report}')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass
        else:
            print("CCMetagen -- Nothing to do here:", {params.runid})
       

rule catbat: #???
    input:
        db = DI['catbat']+"/CAT_prepare_20200618",
        taxonomy = DI['catbat']+"/CAT_prepare_20200618/taxonomy",
        files = "{PATH}/data/{sample}.fastq.gz"
    output:
        #contigs = '{PATH}/result/classification/catbat/contigs/{sample}_{run}.catbat.contigs',
        bins = '{PATH}/result/classification/catbat/bins/{sample}_{run}.catbat.bins',
        name = '{PATH}/result/classification/catbat/bins/renamedBins/{sample}_{run}.catbat.rbins',
        report =  '{PATH}/result/classification/catbat/bins/{sample}_{run}.catbat.report'
    benchmark:
        '{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.catbat.benchmark.txt'
    threads: 8
    params:
	    runid=get_run
    log:
        '{PATH}/result/classification/catbat/{run}/{sample}_{run}.catbat.log'
    conda:
        '{PATH}/result/classificationBenchmark/envs/catbat.yaml'
    run:
        #'CAT contigs -c {input.files} -d {input.db} -t {input.taxonomy} -o {output.contigs}',
        if 'default' in {params.runid}:
            shell('CAT bins -b {input.files} -d {input.db} -t {input.taxonomy} -o {output.bins} -p {output.contigs} -n {threads}'),
            shell('CAT add_names -i {output.bins} -o {output.names} -t {input.taxonomy} --only_official'),
            shell('CAT summarise -i {output.names} -o {output.report}')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass
        else:
            print("CAT&BAT -- Nothing to do here:", {params.runid})
        

rule diamond:
    input:
        #db= DI['diamond']+"/nr",
        files = "{PATH}/data/{sample}.fastq"
    output:
        files='{PATH}/result/classification/diamond/{run}/{sample}_{run}.diamond.classification'
    benchmark:
        '{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.diamond.benchmark.txt'
    threads: 8
    params:
        runid=get_run,
        db = DI['diamond']+"/nr"
    log:
        '{PATH}/result/classification/diamond/{run}/{sample}_{run}.diamond.log'
    conda:
        'envs/diamond.yaml'
    run:
        # 
        if 'default' in {params.runid}:
            shell('diamond blastx --db {params.db} -q {input.files} -o {output.files} -p {threads} --log')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass
        else:
            print("Diamond -- Nothing to do here:", {params.runid})
        


rule metaothello:
    input:
        db = DI['metaothello']+"/bacterial_31mer_L12.index",
        spec2tax = DI['metaothello']+"/bacterial_speciesId2taxoInfo.txt",
        ncbiNames = DI['metaothello']+"/names.dmp.scientific",
        files = "{PATH}/data/{sample}.fastq.gz"
    output:
        '{PATH}/result/classification/metaothello/{run}/{sample}_{run}.metaothello.classification'
    benchmark:
        '{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.metaothello.benchmark.txt'
    threads: 8
    params:
	    runid=get_run
    log:
        '{PATH}/result/classification/metaothello/{run}/{sample}_{run}.metaothello.log'
    conda:
        '{PATH}/result/classificationBenchmark/envs/main.yaml'
    run:
        if 'default' in {params.runid}:
            shell('classifier {input.db} {output} 31 {threads} FA/FQ SE/PE {input.spec2tax} {input.ncbiNames} {input.files}')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass
        else:
            print("MetaOthello -- Nothing to do here:", {params.runid})
