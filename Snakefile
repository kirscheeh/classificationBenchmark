# Snakefile for project work of benchmarking different classification tools regarding their usability for long reads

configfile: "config.yaml"

########## VARIABLE DEFINITION
DI= dict(config["dataIndex"])
PATH = config["path"]
SAMPLES = "gridion364"# gridion366".split(" ")#list(config["samples"])
TOOLS= 'diamond centrifuge kraken2 clark kaiju'.split(" ")#list(config["classification"])
RUNS='default'# medium restrictive'.split()

rule all:
    input:
#       expand("{path}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.report", run=RUNS, sample=SAMPLES, tool=TOOLS, path=PATH),
       expand("{path}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.stats", run=RUNS, sample=SAMPLES, tool=TOOLS, path=PATH),
#       expand("{path}/result/classification/{tool}/{run}/{sample}.{tool}.intermediate", run=RUNS, sample=SAMPLES, tool=TOOLS, path=PATH)
#       expand("{path}/result/classification/{tool}/default/{sample}_{run}.catbat.bins",tool=TOOLS, run=RUNS, sample=SAMPLES, path=PATH)

# creating the project structure
rule create:
    shell:
        'python structure.py'

def get_run(wildcards): #returns the current value of variable/wildcard run
    return wildcards.run

def get_tool(wildcards): #returns the current value of variable/wildcard run
    return wildcards.tool

rule centrifuge:
    input: 
        fastq = "{PATH}/data/{sample}.fastq"
    output:
        files = "{PATH}/result/classification/centrifuge/{run}/{sample}_{run}.centrifuge.classification",
        report= "{PATH}/result/classification/centrifuge/{run}/{sample}_{run}.centrifuge.report"
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.centrifuge.benchmark.txt"
        #repeat("benchmarks/{sample}.bwa.benchmark.txt", 3 für 3 runs
    threads: 8
    params:
        runid=get_run,
	db = DI["centrifuge"]
    log:
        "{PATH}/result/classification/centrifuge/{run}/{sample}_{run}.centrifuge.log"
    conda:
       "envs/centrifuge.yaml"
    run:
        # -q 				files are fastq
    	# -x 				index files
    	# --report-file 	generated report file
    	# -S 				output file
        # -f                query input files are (multi)fasta
        # --ignore-quals
        
        if 'default' in {params.runid}:
            shell('centrifuge -q -x {params.db} {input.fastq} --report-file {output.report} -S {output.files} --ignore-quals')
        elif 'medium' in {params.runid}: 
            print("Sure")
        elif 'restrictive' in {params.runid}: 
            print("Sure")
        else:
            print("Centrifuge -- Nothing to be done here:", {params.runid})

rule kraken2:
    input:
        db = DI['kraken2'],
        files = "{PATH}/data/{sample}.fastq"
    output:
        files = "{PATH}/result/classification/kraken2/{run}/{sample}_{run}.kraken2.classification",
        report= "{PATH}/result/classification/kraken2/{run}/{sample}_{run}.kraken2.report",
        unclassified="{PATH}/result/classification/kraken2/{run}/{sample}_{run}.kraken2.unclassified"
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.kraken2.benchmark.txt"
    threads: 8
    params:
        runid=get_run
    log:
        '{PATH}/result/classification/kraken2/{run}/{sample}_{run}.kraken2.log'
    conda:
        'envs/main.yaml'
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
    threads: 4
    params:
        runid=get_run
    log:
        '{PATH}/result/classification/kaiju/{run}/{sample}_{run}.kaiju.log'
    conda:
        'envs/main.yaml'
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

rule kaiju_summary:
    input:
        nodes = DI['kaiju']+"/nodes.dmp",
        names= DI['kaiju']+"/names.dmp",
        files = "{PATH}/result/classification/kaiju/{run}/{sample}_{run}.kaiju.classification" 
    output:
        "{PATH}/result/classification/kaiju/{run}/{sample}_{run}.kaiju.report"
    conda:
        'envs/main.yaml'
    shell:
        "kaiju2table -t {input.nodes} -n {input.names} -r species -o {output} {input.files}"   

rule taxmaps: # many folders, fix output
    input:
        db = DI['taxmaps']+"/refseq_complete_bacarchvir.lcak300.gem",
        taxonomy = DI['taxmaps']+"/taxonomy.tbl.gz",
        nodes = DI['kaiju']+"/nodes.dmp",
        files = "{PATH}/data/{sample}.fastq"
    benchmark:
        '{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.taxmaps.benchmark.txt'
    output:
        o = '{PATH}/result/classification/taxmaps/{run}/{sample}_{run}.taxmaps.classification',
	folder = '{PATH}/result/classification/taxmaps/{run}/{sample}' 
    threads: 8
    params:
        runid=get_run,
	prefix = "{sample}_{run}.taxmaps.classification"
    log:
        "{PATH}/result/classification/taxmaps/{run}/{sample}_{run}.taxmaps.log"
    conda:
        'envs/taxmaps.yaml' 
    run:
        # -f        input fastq
        # -l        in preprocessing: minimum read length for mapping
        # -C        in preprocessing: entropy cutoff for low complexity filtering
        # -d        index files
        # -t        taxonomic rable
        # --cov     coverage histogram
        # -o        output directory
        if 'default' in {params.runid}:
            shell('export PERL5LIB=/home/re85gih/miniconda3/envs/taxmaps/opt/krona/lib/'),
            shell('export PATH=$PATH:/home/re85gih/projectClassification/taxmaps/'),
            shell('taxMaps -f {input.files} -c {threads} -t {input.taxonomy} -d {input.db} -o {output.folder} -p {params.prefix}')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass   
        else:
            print("TaxMaps -- Nothing to do here:", {params.runid}) 

rule deepmicrobes: 
    input:
        files = "{PATH}/data/{sample}.fastq",
        kmers =DI["deepmicrobes"]+"/tokens_merged_12mers.txt",
        weights=DI["deepmicrobes"]+"/weights_species",
        name2label=DI["deepmicrobes"]+"/name2label_species.txt"
    output:
        prediction="{PATH}/result/classification/deepmicrobes/{run}/{sample}_{run}.deepmicrobes.prediction.tfrec",
        tfrec="{PATH}/result/classification/deepmicrobes/{run}/{sample}_{run}.deepmicrobes.training.tfrec",
        classification="{PATH}/result/classification/deepmicrobes/{run}/{sample}_{run}.deepmicrobes.classification",
        report="{PATH}/result/classification/deepmicrobes/{run}/{sample}_{run}.deepmicrobes.report"
    conda:
        'envs/deepmicrobes.yaml'
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.deepmicrobes.benchmark.txt"
    threads: 8
    run:
        # --kmer        length of k-mers (default: 12) --> if i want to change that i might need to build my own index
        # --max_len     max length of sequences (default: 150)
        # --pred_out    path to prediction output
        # -dd           location of input data
        # -ebe          number of training epochs to run between evaluations
        # just for me now
        
        shell('export PATH=/home/re85gih/projectClassification/DeepMicrobes/pipelines:$PATH'),
        shell('export PATH=/home/re85gih/projectClassification/DeepMicrobes/scripts:$PATH'),
        shell('export PATH=/home/re85gih/projectClassification/DeepMicrobes:$PATH'),
        
        # transform training fastq to tfrec
        #shell('tfrec_train_kmer.sh -i {input.files} -v {input.kmers} -o {output.tfrec}'),
        
        # transform prediction fastq to tfrec
        shell('tfrec_predict_kmer.sh -f {input.files} -t fastq -v {input.kmers} -o {output.prediction}'),
        
        # make prediction on metagenome datasaet
        shell('predict_DeepMicrobes.sh -i {output.prediction} -l species -p 8 -m {input.weights} -o {output.classification}'), 
        
        # generate taxonomic profiles
        shell('report_profile.sh -i {output.classification} -o {output.report} -t 50 -l {input.name2label}')

rule kslam:
    input:
        db = DI['kslam'],
        files = "{PATH}/data/{sample}.fastq"
    output:
        "{PATH}/result/classification/kslam/{run}/{sample}_{run}.kslam.classification" 
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.kslam.benchmark.txt"
    threads: 16
    params:
        runid=get_run
    log:
        "{PATH}/result/classification/kslam/{run}/{sample}_{run}.kslam.log"
    conda:
        'envs/kslam.yaml'
    run:
        # --db                      database file
        # --min-alignment-score     alignment score cutoff
        if 'default' in {params.runid}:
            shell('SLAM --db={input.db} --output-file={output} --num-reads-at-once 1000000 {input.files}')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass
        else:
            print("KSLAM -- Nothing to do here:", {params.runid})
        
rule clark: #output is csv, watch out
    input:
        #db = DI['clark']+"/",
        files = "{PATH}/data/{sample}.fastq",
	targets = "/mnt/fass1/database/clark_database/targets.txt"
    output:
        files = "{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification" 
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.clark.benchmark.txt"
    threads: 8
    params:
            db = "/mnt/fass1/kirsten/database/clark/",
	    runid=get_run
    log:
        "{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.log"
    conda:
        'envs/main.yaml'
    run:
        # -k        k-mer size, has to be between 2 and 32, default:31 
        # --long    for long reads (only for full mode)
        # -m        mode of execution

        if 'default' in {params.runid}:
            shell('CLARK --long -O {input.files} -R {output} -D {input.db} -n {threads} -T {input.targets}')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass
        else:
            print("CLARK -- Nothing to do here:", {params.runid})

rule clark_abundance:
    input:
        res="{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification.csv"
    output:
        "{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.report"
    params:
        db = DI['clark']+"/",
        unnamed="{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification"
    conda:
        'envs/main.yaml'    
    run:
        shell("{PATH}/result/classificationBenchmark/scripts/clark.estimate_abundance.sh -F {input.res} -D {params.db} > {output}"),
        shell("mv {input.res} {params.unnamed}")
        
# preprocessing for ccmetagen
rule kma:
    input:
        #db = DI['ccmetagen']+"compress_ncbi_nt/ncbi_nt",
        files = "{PATH}/data/{sample}.fastq"
    output:
        "{PATH}/result/classification/ccmetagen/{sample}.kma.intermediate.res",
        "{PATH}/result/classification/ccmetagen/{sample}.kma.intermediate.mapstat"
    benchmark:
        "{PATH}/result/classification/benchmarks/{sample}.kma.benchmark.txt"
    threads: 8
    log:
        "{PATH}/result/classification/ccmetagen/{sample}.kma.log"
    conda:
        'envs/main.yaml'
    params:
        db = DI['ccmetagen']+"/compress_ncbi_nt/ncbi_nt"
    shell:
        'kma -i {input.files} -t_db {params.db} -o {output} -t {threads} -1t1 -mem_mode -and -ef'

rule ccmetagen: #watch output 
    input:
        kma = "{PATH}/result/classification/ccmetagen/{sample}.kma.intermediate.res",
        files = "{PATH}/data/{sample}.fastq",
        mapstat="{PATH}/result/classification/ccmetagen/{sample}.kma.intermediate.mapstat"
    output:
        files = "{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.classification.csv",
        test="{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.classification_stats.csv"
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.ccmetagen.benchmark.txt"
    threads: 8
    params:
	    runid=get_run,
            output="{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.classification"
    log:
        "{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.log"
    conda:
        'envs/main.yaml'
    run:
        # -m    mode
        # -r    reference database
        # -i    path to kma result
        # -ef   extended output file that includes percentage of classified reads
        # -c    minimum coverage
        if 'default' in {params.runid}:
            shell('CCMetagen.py -o {params.output} -i {input.kma} -ef y --map {input.mapstat}')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass
        else:
            print("CCMetagen -- Nothing to do here:", {params.runid})

rule rename_ccmetagen:
    input:
        report="{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.classification_stats.csv",
        classi="{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.classification.csv"
    output:
        report="{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.report",
        classi="{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.classification"
    run:
        shell("mv {input.report} {output.report}"),
        shell("mv {input.classi} {output.classi}")

rule catbat: #???
    input:
        db = DI['catbat']+"/2020-06-18_CAT_database",
        taxonomy = DI['catbat']+"/2020-06-18_taxonomy",
        files = "{PATH}/data/{sample}.fastq"
    output:
        #contigs = "{PATH}/result/classification/catbat/contigs/{sample}_{run}.catbat.contigs",
        bins = "{PATH}/result/classification/catbat/default/{sample}_{run}.catbat.bins",
        #name = "{PATH}/result/classification/catbat/bins/renamedBins/{sample}_{run}.catbat.rbins",
        #report = "{PATH}/result/classification/catbat/bins/{sample}_{run}.catbat.report",
	output="{PATH}/result/classification/catbat/default/{sample}_{run}.out.CAT.ORF2LCA.txt"
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.catbat.benchmark.txt"
    threads: 8
    params:
	    runid=get_run
    log:
        "{PATH}/result/classification/catbat/{run}/{sample}_{run}.catbat.log"
    conda:
        'envs/catbat.yaml'
    run:
        #'CAT contigs -c {input.files} -d {input.db} -t {input.taxonomy} -o {output.contigs}',
        if 'default' in {params.runid}:
            #shell('CAT contigs -c {input.files} -d {input.db} -t {input.taxonomy} -o {output.contigs}')
            shell('CAT bins -b {input.files} -d {input.db} -t {input.taxonomy} -o {output.bins} -n {threads}')
            #shell('CAT add_names -i {output.bins} -o {output.names} -t {input.taxonomy} --only_official'),
            #shell('CAT summarise -i {output.names} -o {output.report}')
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
        files="{PATH}/result/classification/diamond/{run}/{sample}_{run}.diamond.classification"
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.diamond.benchmark.txt"
    threads: 8
    params:
        runid=get_run,
        db = DI['diamond']+"/nr"
    log:
        '{PATH}/result/classification/diamond/{run}/{sample}_{run}.diamond.log'
    conda:
        'envs/diamond.yaml'
    run:
        # --outfmt defines format as taxonomic classification
        if 'default' in {params.runid}:
            shell('diamond blastx --db {params.db} -q {input.files} -o {output.files} -p {threads} --log --outfmt 102')
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
        files = "{PATH}/data/{sample}.fastq"
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
        'envs/main.yaml'
    run:
        if 'default' in {params.runid}:
            shell('/home/re85gih/projectClassification/metaOthello/classifier/classifier {input.db} {output} 31 {threads} FQ SE {input.spec2tax} {input.ncbiNames} {input.files}')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass
        else:
            print("MetaOthello -- Nothing to do here:", {params.runid})

rule areport:
    input: 
        classification = "{PATH}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.classification"
    output:
        areport="{PATH}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.areport",
        #stats="{PATH}/result/classificationBenchmark/stats/{sample}_{run}.{tool}.stats"
    params:
        report="{PATH}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.report",
        tool=get_tool,
	script="{PATH}/result/classificationBenchmark/scripts/processingOutput/"
    run:
        print({params.tool}, {params.report})
        if 'centrifuge' in {params.tool} or 'kaiju' in {params.tool} or 'clark' in {params.tool}:
            #print("{params.script}{params.tool}Output.py {input.classification} {params.report} {output.areport}")
            shell('python {params.script}{params.tool}Output.py {input.classification} {params.report} {output.areport}')
        elif 'ccmetagen' in {params.tool} or 'kraken2' in {params.tool}:
            #print({params.tool}, "{params.script}{params.tool}Output.py {params.report} {output.areport}")
            shell('python {params.script}{params.tool}Output.py {params.report} {output.areport}')
        elif 'diamond' in {params.tool} or 'kslam' in {params.tool}:
            shell('python {params.script}{params.tool}Output.py {input.classification} {output.areport}')

rule stats:
    input: 
        areport = "{PATH}/result/{sample}_{run}.{tool}.areport"
    output:
        stats="{PATH}/result/{sample}_{run}.{tool}.stats"
    conda:
        "envs/main.yaml"
    params:
        tool=get_tool,
        script="{PATH}/result/classificationBenchmark/scripts/calcAUPR.py"
    shell:
        "python3.8 {params.script} {input.areport} config.yaml {output.stats}"
