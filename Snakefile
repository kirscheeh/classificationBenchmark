# Snakefile for project work of benchmarking different classification tools regarding their usability for long reads
import scripts.getting as getting

configfile: "config.yaml"

########## VARIABLE DEFINITION ##########
DB_default=dict(config["DB_default"])
DB_custom= dict(config["DB_custom"])

PATH = config["path"]

SAMPLES =list(config["samples"])
TOOLS="clark" # .split(" ") #'diamond centrifuge kraken2 kaiju'.split(" ") #list(config["classification"])
RUNS='custom'# custom customHit'.split(" ")

rule all:
    input:
# CLASSIFICATION 
#        expand("/mnt/fass2/projects/kirsten/{sample}_{run}.{tool}.classification", run=RUNS, sample=SAMPLES, tool=TOOLS, path=PATH),
## KMA (for CCMetagen)
#        expand("{path}/result/classification/ccmetagen/{run}/{sample}_{run}.kma.res", run=RUNS, sample=SAMPLES, path=PATH),
## for CLARK-Output
        expand("/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.clark.classification.csv", run=RUNS, sample=SAMPLES, path=PATH),
# REPORT
        expand("/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.{tool}.report", run=RUNS, sample=SAMPLES, tool=TOOLS, path=PATH),
# GENERATING (comparable) REPORTS
        expand("/mnt/fass2/projects/kirsten/{sample}_{run}.{tool}.areport", run=RUNS, sample=SAMPLES, tool=TOOLS, path=PATH),
# PIECHARTS
#        expand("{path}/result/classification/stats/{run}/{sample}_{run}.{tool}.piechart.png", run=RUNS, sample=SAMPLES, tool=TOOLS, path=PATH),
# PRECISION RECALL CURVE
#        expand("{path}/result/classification/stats/{run}/{sample}_{run}.{tool}.prc.jpeg",run=RUNS, sample=SAMPLES, tool=TOOLS, path=PATH),
# ABUNANCE PROFILE SIMILARITY
#        expand("{path}/result/classification/stats/{run}/{sample}_{run}.{tool}.truthEven.aps", run=RUNS, sample=SAMPLES, tool=TOOLS, path=PATH)

# creating the project structure
rule create:
    shell:
        'python setup.py'

def get_run(wildcards): #returns the current value of variable/wildcard run
    return wildcards.run

def get_tool(wildcards): #returns the current value of variable/wildcard run
    return wildcards.tool

def get_medianHitLength(wildcards):
    if "medianHitLength" in wildcards.run:
        return scripts.getting.get_seqLength(str(PATH[0])+"/data/"+str(wildcards.sample)+".fastq")/2
    else:
        return 22 # default 

def get_sample(wildcards):
    return wildcards.sample

rule centrifuge:
    input: 
        fastq = "{PATH}/data/{sample}.fastq"
    output:
        files = "{PATH}/result/classification/centrifuge/{run}/{sample}_{run}.centrifuge.classification",
        report= "{PATH}/result/classification/centrifuge/{run}/{sample}_{run}.centrifuge.report"
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.centrifuge.benchmark.txt"
    threads: 8
    conda:
       "envs/centrifuge.yaml"
    params:
        runID=get_run,
	    dbDefault = DB_default["centrifuge"],
        dbCustom = DB_custom["centrifuge"],
        medianlength=get_medianHitLength
    run:
        # -q 				files are fastq
    	# -x 				index files
    	# --report-file 	generated report file
    	# -S 				output file
        # -f                query input files are (multi)fasta
        # --ignore-quals    treat all quality values as 30 on Phred scale
        
        if 'default' in {params.runID}:
            shell('centrifuge -q -x {params.dbDefault} {input.fastq} --report-file {output.report} -S {output.files}')
        elif 'custom' in {params.runID}:
            shell('centrifuge -q -x {params.dbCustom} {input.fastq} --report-file {output.report} -S {output.files}')
        elif 'customHit' in {params.runID}:  # no default hit length
             shell('centrifuge -q -x {params.dbDefault} {input.fastq} --report-file {output.report} -S {output.files} --ignore-quals --min-hit-length {params.medianlength}')
        else:
            print("Centrifuge -- Nothing to be done here:", {params.runID})
        #  elif 'quals' in {params.runID}: shell('centrifuge -q -x {params.db} {input.fastq} --report-file {output.report} -S {output.files} --ignoreQuals')

rule kraken2:
    input:
        files = "{PATH}/data/{sample}.fastq"
    output:
        files = "{PATH}/result/classification/kraken2/{run}/{sample}_{run}.kraken2.classification",
        report = "{PATH}/result/classification/kraken2/{run}/{sample}_{run}.kraken2.report",
        unclassified = "{PATH}/result/classification/kraken2/{run}/{sample}_{run}.kraken2.unclassified"
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.kraken2.benchmark.txt"
    threads: 8
    conda:
        "envs/main.yaml"    
    params:
        runID=get_run,
        dbDefault=DB_default['kraken2'],
        dbCustom=DB_custom['kraken2']
    run:
        # --confidence          threshold that must be in [0,1]
        # --unclassified-out    prints unclassified sequences to filename
        # --classified-out      prints classified sequences to filename
        # --output              prints output to filename
        # --report              prints report with aggregate counts/clade to file
        
        if 'default' in {params.runID}:
            shell('kraken2 --db {params.dbDefault} --unclassified-out {output.unclassified} --report {output.report} --threads {threads} --output {output.files} {input.files}')
        elif 'customHit' in {params.runID}: # confidence set after benchmark paper
            shell('kraken2 --db {input.dbCustom} --report {output.report} --confidence 0.05 --threads {threads} --output {output.files} {input.files}')
        elif 'custom' in {params.runID}: 
            shell('kraken2 --db {params.dbCustom} --unclassified-out {output.unclassified} --report {output.report} --threads {threads} --output {output.files} {input.files}')
            print("Sure") 
        else:
            print("Kraken2 -- Nothing to do here:", {params.runID})           

rule kaiju:
    input:
        fastq = "{PATH}/data/{sample}.fastq"
    output:
        files = '{PATH}/result/classification/kaiju/{run}/{sample}_{run}.kaiju.classification'
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.kaiju.benchmark.txt"
    threads: 8
    conda:
        "envs/main.yaml"
    params:
        runID=get_run,
        medianHitLength=get_medianHitLength,
        dbDefault = DB_default['kaiju']+"/kaiju_db_refseq.fmi",
        dbCustom = DB_custom['kaiju']+"/refseqBacFung.kaiju.fmi",
        nodes = DB_default['nodes'],
    run:
        # -t    name of nodes.dmp file
        # -f    name of database (.fmi) file
        # -i    input file containing fasta/fastq
        # -o    name of output file  
        # -m    minimum match length (default: 11)        
        if 'default' in {params.runID}:
            shell('kaiju -t {params.nodes} -f {params.dbDefault} -i {input.fastq} -o {output.files} -z {threads} -v')
        if 'custom' in {params.runID}:
            shell('kaiju -t {params.nodes} -f {params.dbCustom} -i {input.fastq} -o {output.files} -z {threads} -v')
        elif 'customHit' in {params.runID}:
            shell('kaiju -t {params.nodes} -f {params.dbCustom} -i {input.files} -o {output.fastq} -z {threads} -v -m {params.medianHitLength}')
        else:
            print("Kaiju -- Nothing to do here:", {params.runID})

rule kaiju_summary:
    input:
        nodes = DB_default['nodes'],
        names= DB_default['names'],
        files = "{PATH}/result/classification/kaiju/{run}/{sample}_{run}.kaiju.classification" 
    output:
        "{PATH}/result/classification/kaiju/{run}/{sample}_{run}.kaiju.report"
    conda:
        "envs/main.yaml"
    shell:
        "kaiju2table -t {input.nodes} -n {input.names} -r species -o {output} {input.files}"   

        
rule clark:
    input:
        fastq =  "/mnt/fass1/kirsten/data/{sample}.fastq",
        targets = DB_custom["clark_targets"] #"/mnt/fass1/database/clark_database/targets.txt"
    output:
        csv = "/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.clark.classification.csv",  # "{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification.csv",
        #stats="{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification_stats.csv" 
    benchmark:
        "/mnt/fass1/kirsten/result/classification/benchmarks/{run}/{sample}_{run}.clark.benchmark.txt" # "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.clark.benchmark.txt"
    threads: 8
    conda:
        "envs/main.yaml"
    params:
        dbDefault = DB_default["clark"],
        dbCustom = DB_custom["clark"],
        runID=get_run,
        result = "/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.clark.classification" # "{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification"
    run:
        # --long    for long reads (only for full mode)
        # -t        minimum of k-mer frequency/occurence for the discriminative k-mers (default:0)

        if 'default' in {params.runID}:
            shell('CLARK --long -O {input.fastq} -R {params.result} -D {params.dbDefault} -n {threads} -T {input.targets}')
        elif 'custom' in {params.runID}:
            shell('CLARK-l --long -O {input.fastq} -R {params.result} -D {params.dbCustom} -n {threads} -T {input.targets}')
        elif 'customHit' in {params.runID}:
            shell('CLARK --long -O {input.fastq} -R {params.result} -D {params.dbCustom} -n {threads} -T {input.targets} -t 2')
        else:
            print("CLARK -- Nothing to do here:", {params.runID})

rule clark_abundance:
    input:
        "/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.clark.classification.csv" # "{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification.csv"
    output:
        report= "/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.clark.report",
 # "{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.report",
        #unnamed="{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification"
    params:
        taxonomy=DB_default['clark_taxonomy'],       
      # dbDefault = DB_default["clark"], #"/mnt/fass1/database/clark_database",
        #dbCustom = DB_custom["clark"],
        runID=get_run,
        unnamed= "/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.clark.classification" #"{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification"
    conda:
        "envs/main.yaml"    
    run:
        if 'default' in {params.runID}:
            shell("/mnt/fass1/kirsten/result/classificationBenchmark/scripts/clark.estimate_abundance.sh -F {input} -D {params.taxonomy} > {output}"),
            shell("mv {input.res} {params.unnamed}")
        else:
            shell("/mnt/fass1/kirsten/result/classificationBenchmark/scripts/clark.estimate_abundance.sh -F {input} -D {params.taxonomy} > {output}"),
            shell("mv {input.res} {params.unnamed}")

rule taxmaps: # many folders, fix output
    input:
        dbDefault = DB_default['taxmaps']+"/refseq_complete_bacarchvir.lcak300.gem",
        taxonomy = DB_default['taxmaps']+"/taxonomy.tbl.gz",
        nodes = DB_default['nodes'],
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
            shell('taxMaps -f {input.files} -c {threads} -t {input.taxonomy} -d {input.dbDefault} -o {output.folder} -p {params.prefix}')
        elif 'medium' in {params.runid}:
            pass
        elif 'restrictive' in {params.runid}:
            pass   
        else:
            print("TaxMaps -- Nothing to do here:", {params.runid})
        
# preprocessing for ccmetagen
rule kma:
    input:
        "{PATH}/data/{sample}.fastq"
    output:
        result = "{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.kma.res",
        mapstat = "{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.kma.mapstat"
    benchmark:
        "{PATH}/result/classification/benchmarks/{sample}_{run}.kma.benchmark.txt"
    conda:
        "envs/main.yaml"
    threads: 8
    params:
        dbDefault = DB_default["ccmetagen"]+"/ncbi_nt",
        dbCustom = DB_custom["ccmetagen"],
        result="{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.kma.intermediate",
        sample=get_sample,
        runID=get_run,
        script="{PATH}/result/classificationBenchmark/scripts/ccmetagen.piecer.sh"
    run:
        if 'promethion' in {params.sample}:
            shell('{params.script} {input} helper.fastq {params.dbDefault} {output.result}')
        else:
            shell('kma -i {input} -t_db {params.dbDefault} -o {output.result} -t {threads} -1t1 -mem_mode -and -ef')

rule ccmetagen:
    input:
        kma = "{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.kma.res",
        #fastq = "{PATH}/data/{sample}.fastq",
        mapstat = "{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.kma.mapstat"
    output:
        "{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.classification.csv",
        "{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.classification_stats.csv"
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.ccmetagen.benchmark.txt"
    threads: 8
    conda:
        "envs/main.yaml"
    params:
        runID=get_run,
        result="{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.ccmetagen.classification"
    run:
        # -i    path to kma result
        # -ef   extended output file that includes percentage of classified reads
        # -c    minimum coverage

        if 'default' in {params.runID} or 'custom' in {params.runID}:
            shell('CCMetagen.py -o {params.output} -i {input.kma} -ef y --map {input.mapstat}')
        elif 'customHit' in {params.runID}: # is there any option? --d 0.4?
            shell('CCMetagen.py -o {params.output} -i {input.kma} -ef y --map {input.mapstat} -c 40')
        else:
            print("CCMetagen -- Nothing to do here:", {params.runID})

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

rule diamond:
    input:
        files = "/mnt/fass1/kirsten/data/{sample}.fastq" # "{PATH}/data/{sample}.fastq"
    output:
        files="/mnt/fass2/projects/kirsten/{sample}_{run}.{tool}.classification" #files="{PATH}/result/classification/diamond/{run}/{sample}_{run}.diamond.classification"
    benchmark:
       "/mnt/fass1/kirsten/result/classification/benchmarks/{run}/{sample}_{run}.diamond.benchmark.txt"  #"{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.diamond.benchmark.txt"
    threads: 8
    conda:
        "envs/diamond.yaml"
    params:
        runID=get_run,
        dbDefault = DB_default["diamond"],#+"/nr"
        dbCustom = DB_custom["diamond"],
	# medianHitLength=get_medianHitLength
    run:
        # --outfmt defines format as taxonomic classification
        # --more-sensitive more sensitive than sensitive, which is <40% identity
        
        if 'default' in {params.runID}:
            shell('diamond blastx --db {params.dbDefault} -q {input.files} -o {output.files} -p {threads} --outfmt 102')
        elif 'custom' in {params.runID}:
            shell('diamond blastx --db {params.dbCustom} -q {input.files} -o {output.files} -p {threads} --outfmt 102 -b1.0')
        elif 'customHit' in {params.runID}:
            shell('diamond blastx --db {params.dbCustom} -q {input.files} -o {output.files} -p {threads} --outfmt 102 --id {params.medianHitLength}')
        else:
            print("Diamond -- Nothing to do here:", {params.runID})

rule areport:
    input: 
        classification = "/mnt/fass2/projects/kirsten/{sample}_{run}.{tool}.classification" #"{PATH}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.classification"
    output:
        areports="/mnt/fass2/projects/kirsten/{sample}_{run}.{tool}.areport"        
        #areport="{PATH}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.areport"
    conda:
        "envs/main.yaml"
    params:
        #report="{PATH}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.report",
        #report="/mnt/fass2/projects/kirsten/{sample}_{run}.{tool}.report",
        tool=get_tool,
	    script="/mnt/fass1/kirsten/result/classificationBenchmark/scripts/" # "{PATH}/result/classificationBenchmark/scripts/"
    run:
        print({params.tool}, {params.report})
        if 'diamond' in {params.tool}:
            shell('python {params.script}{params.tool}Output.py {input.classification} {output.areport}')
        elif 'centrifuge' in {params.tool}:
            shell('python {params.script}{params.tool}Output.py {input.classification} {params.report} {output.areport}')
        else: 
            shell('python {params.script}{params.tool}Output.py {params.report} {output.areport}')
        
rule piechart:
    input:
        "{PATH}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.areport"
    output:
        "{PATH}/result/classification/stats/{run}/{sample}_{run}.{tool}.piechart.png"
    conda:
        "envs/main.yaml"
    params:
        "{PATH}/result/classificationBenchmark/scripts/classificationPiecharts.R"
    shell:
        'Rscript {params} {input} {output}'

rule prc: #recision recall curve
    input:
        "{PATH}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.areport"
    output:
        "{PATH}/result/classification/stats/{run}/{sample}_{run}.{tool}.prc.jpeg"
    conda:
        "envs/renv.yaml"
    params:
        "{PATH}/result/classificationBenchmark/scripts/PRCurve.sh"
    shell:
        '{params} {input} {output}'

rule aps: # abundance profile similarity
    input:
        "{PATH}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.areport"
    output:
        "{PATH}/result/classification/stats/{run}/{sample}_{run}.{tool}.truthEven.aps"
       # estimate="{PATH}/result/classification/stats/{run}/{sample}_{run}.estimate.aps",
       # truthLog ="{PATH}/result/classification/stats/{run}/{sample}_{run}.truthLog.aps"
    conda:
        "envs/main.yaml"
    params:
        script="{PATH}/result/classificationBenchmark/scripts/abundanceProfile.sh",
        truthEven="{PATH}/result/classification/stats/{run}/{sample}_{run}.truthEven.aps",
        estimate = "{PATH}/result/classification/stats/{run}/{sample}_{run}.estimate.aps",
        truthLog="{PATH}/result/classification/stats/{run}/{sample}_{run}.truthLog.aps"
    run:
        if getting.get_sampleName(str({input})) in ['gridion364', 'promethion365']:
            shell("{params.script} {input} [0.12,0.12,0.12,0.12,0.12,0.12,0.12,0.12,0.02,0.02] {params.truthEven}"),
            shell("{params.script} {input} [0.1932,0.1456,0.1224,0.1128,0.0999,0.0993,0.097,0.0928,0.0192,0.0178] {params.estimate}")
        else:
            shell("{params.script} {input} [0.0089, 0.891, 0.0000089, 0.00000089, 0.00089, 0.00089, 0.089, 0.000089, 0.0089, 0.000089] {params.truthLog}")
