# Snakefile for project work of benchmarking different classification tools regarding their usability for long reads
configfile: "config.yaml"

########## VARIABLE DEFINITION ##########
DB_default=dict(config["DB_default"])
DB_custom= dict(config["DB_custom"])

PATH = config["path"]

SAMPLES = list(config["samples"])
TOOLS = list(config["classification"])
RUNS = 'custom default'. split(" ") # not used: customHit

TOOLS_WO_C = "diamond kaiju ccmetagen centrifuge kraken2".split(" ") # needed for classification
TOOLS_W_REPORT = "kaiju ccmetagen clark".split(" ") # tools that generate ereport externally

#         expand("/mnt/fass2/projects/kirsten/diamond/{sample}_{run}.{tool}.classification", run=RUNS, sample=SAMPLES, tool=TOOLS, path=PATH), # /mnt/fass2/projects/kirsten/ # {path}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.classification

rule all:
    input:
# KMA (for CCMetagen)
        expand("{path}/result/classification/ccmetagen/{run}/{sample}_{run}.kma.res", run=RUNS, sample=SAMPLES, path=PATH),
# CLASSIFICATION 
        expand('{path}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.classification', run=RUNS, sample=SAMPLES, tool=TOOLS_WO_C, path=PATH),
## for CLARK classification
        expand('{path}/result/classification/clark/{run}/{sample}_{run}.clark.classification.csv', run=RUNS, sample=SAMPLES, path=PATH), # "/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.clark.classification.csv"
# REPORT (some tools)
        expand("{path}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.report", run=RUNS, sample=SAMPLES, tool=TOOLS_W_REPORT, path=PATH), # "/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.{tool}.report"
# GENERATING (comparable) REPORTS --> areport
        expand('{path}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.areport', run=RUNS, sample=SAMPLES, tool=TOOLS, path=PATH), #/mnt/fass2/projects/kirsten/diamond/{sample}_{run}.{tool}.areport

# creating the project structure
rule create:
    shell:
        'python setup.py'

def get_run(wildcards): #returns the current value of variable/wildcard run
    return wildcards.run

def get_tool(wildcards): #returns the current value of variable/wildcard run
    return wildcards.tool

#def get_medianHitLength(wildcards): NOT USED
#   import scripts.getting as getting
#   if "medianHitLength" in wildcards.run:
#       return scripts.getting.get_seqLength(str(PATH[0])+"/data/"+str(wildcards.sample)+".fastq")/2
#   else:
#       return 22 # default 

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
        #medianlength=get_medianHitLength
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
        # --classified-out      prints classified sequences to filename
        # --output              prints output to filename
        # --report              prints report with aggregate counts/clade to file
        
        if 'default' in {params.runID}:
            shell('kraken2 --db {params.dbDefault}  --report {output.report} --threads {threads} --output {output.files} {input.files}')
        elif 'customHit' in {params.runID}: # confidence set after benchmark paper
            shell('kraken2 --db {input.dbCustom} --report {output.report} --confidence 0.05 --threads {threads} --output {output.files} {input.files}')
        elif 'custom' in {params.runID}: 
            shell('kraken2 --db {params.dbCustom} --report {output.report} --threads {threads} --output {output.files} {input.files}')
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
        dbDefault = DB_default['kaiju']+"/kaiju_db_refseq.fmi",
        dbCustom = DB_custom['kaiju']+"/refseqBacFung.kaiju.fmi",
        nodesDefault = DB_default['kaiju']+"/nodes.dmp",
        nodesCustom = DB_custom['nodes'],
        # medianHitLength=get_medianHitLength,
    run:
        # -t    name of nodes.dmp file
        # -f    name of database (.fmi) file
        # -m    minimum match length (default: 11)        
        if 'default' in {params.runID}:
            shell('kaiju -t {params.nodesDefault} -f {params.dbDefault} -i {input.fastq} -o {output.files} -z {threads} -v')
        if 'custom' in {params.runID}:
            shell('kaiju -t {params.nodesCustom} -f {params.dbCustom} -i {input.fastq} -o {output.files} -z {threads} -v')
        elif 'customHit' in {params.runID}:
            shell('kaiju -t {params.nodesCustom} -f {params.dbCustom} -i {input.files} -o {output.fastq} -z {threads} -v -m {params.medianHitLength}')
        else:
            print("Kaiju -- Nothing to do here:", {params.runID})

rule kaiju_summary:
    input:
        nodesDefault = DB_default['kaiju']+"/nodes.dmp",
        namesDefault = DB_default['kaiju']+"/names.dmp",
        nodesCustom = DB_custom['nodes'],
        namesCustom = DB_custom['names'],
        files = "{PATH}/result/classification/kaiju/{run}/{sample}_{run}.kaiju.classification",
        runID=get_run 
    output:
        "{PATH}/result/classification/kaiju/{run}/{sample}_{run}.kaiju.report"
    conda:
        "envs/main.yaml"
    run:
        if 'default' in {params.runID}:
            shell("kaiju2table -t {input.nodesDefault} -n {input.namesDefault} -r species -o {output} {input.files}")
        else:
            shell("kaiju2table -t {input.nodesCustom} -n {input.namesCustom} -r species -o {output} {input.files}")

        
rule clark:
    input:
        fastq = "{PATH}/data/{sample}.fastq"
        # fastq = "/mnt/fass1/kirsten/data/{sample}.fastq"
    output:
        "{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification.csv" 
        #"/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.clark.classification.csv"
    benchmark:
        "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.clark.benchmark.txt" 
        # "/mnt/fass1/kirsten/result/classification/benchmarks/{run}/{sample}_{run}.clark.benchmark.txt" # 
    threads: 8
    conda:
        "envs/main.yaml"
    params:
        dbDefault = DB_default["clark"],
        dbCustom = DB_custom["clark"],
        targetsDefault = DB_default["clark_targets"],
        targetsCustom = DB_custom["clark_targets"],
        runID=get_run,
        result = "{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification" #  "/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.clark.classification"
    run:
        # --long    for long reads (only for full mode)
        # -t        minimum of k-mer frequency/occurence for the discriminative k-mers (default:0)
        if 'default' in {params.runID}:
            shell('CLARK --long -O {input.fastq} -R {params.result} -D {params.dbDefault} -n {threads} -T {params.targetsDefault}')
        elif 'custom' in {params.runID}:
            shell('CLARK-l --long -O {input.fastq} -R {params.result} -D {params.dbCustom} -n {threads} -T {params.targetsCustom}')
        elif 'customHit' in {params.runID}:
            shell('CLARK --long -O {input.fastq} -R {params.result} -D {params.dbCustom} -n {threads} -T {params.targetsCustom} -t 2')
        else:
            print("CLARK -- Nothing to do here:", {params.runID})

rule clark_abundance:
    input:
        "{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification.csv" # "/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.clark.classification.csv" 
    output:
        report="{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.report", #"/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.clark.report"
        un="{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification"
    params:
        taxonomyDefault = DB_default['clark_taxonomy'],  
        taxonomyCustom =DB_custom['clark_taxonomy'],     
        runID=get_run,
        unnamed= "{PATH}/result/classification/clark/{run}/{sample}_{run}.clark.classification" #"/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.clark.classification"
    conda:
        "envs/main.yaml"    
    run:
        if 'default' in {params.runID}:
            shell("/mnt/fass1/kirsten/result/classificationBenchmark/scripts/clark.estimate_abundance.sh -F {input} -D {params.taxonomyDefault} > {output}"),
            shell("mv {input.report} {params.unnamed}")
        else:
            shell("/mnt/fass1/kirsten/result/classificationBenchmark/scripts/clark.estimate_abundance.sh -F {input} -D {params.taxonomyCustom} > {output}"),
            shell("mv {input.report} {params.unnamed}")
        
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
        dbDefault = DB_default["ccmetagen"],
        dbCustom = DB_default["ccmetagen"],
        result="{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.kma.intermediate",
        sample=get_sample,
        runID=get_run,
    run:
        if 'default' in {params.runID}:
            shell('kma -i {input} -t_db {params.dbDefault} -o {output.result} -t {threads} -1t1 -mem_mode -and -ef')
        else: #unused
            shell('kma -i {input} -t_db {params.dbCustom} -o {output.result} -t {threads} -1t1 -mem_mode -and -ef')

rule ccmetagen:
    input:
        kma = "{PATH}/result/classification/ccmetagen/{run}/{sample}_{run}.kma.res",
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
            shell('CCMetagen.py -o {params.result} -i {input.kma} -ef y --map {input.mapstat}')
        elif 'customHit' in {params.runID}: # is there any option? --d 0.4?
            shell('CCMetagen.py -o {params.result} -i {input.kma} -ef y --map {input.mapstat} -c 40')
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
        files = "{PATH}/data/{sample}.fastq" 
        # files = "/mnt/fass1/kirsten/data/{sample}.fastq" 
    output:
        files="{PATH}/result/classification/diamond/{run}/{sample}_{run}.diamond.classification" 
        # files="/mnt/fass2/projects/kirsten/diamond/{sample}_{run}.{tool}.classification"
    benchmark:
       "{PATH}/result/classification/benchmarks/{run}/{sample}_{run}.diamond.benchmark.txt" 
       #"/mnt/fass1/kirsten/result/classification/benchmarks/{run}/{sample}_{run}.diamond.benchmark.txt" 
    threads: 8
    conda:
        "envs/diamond.yaml"
    params:
        runID=get_run,
        dbDefault = DB_default["diamond"],
        dbCustom = DB_custom["diamond"],
	    # medianHitLength=get_medianHitLength
    run:
        # --outfmt defines format as taxonomic classification
        # --more-sensitive more sensitive than sensitive, which is <40% identity
        
        if 'default' in {params.runID}:
            shell('diamond blastx --db {params.dbDefault} -q {input.files} -o {output.files} -p {threads} --outfmt 102')
        elif 'custom' in {params.runID}:
            shell('diamond blastx --db {params.dbCustom} -q {input.files} -o {output.files} -p {threads} --outfmt 102 -b1.0 -t /home/re85gih/projectClassification')
        elif 'customHit' in {params.runID}:
            shell('diamond blastx --db {params.dbCustom} -q {input.files} -o {output.files} -p {threads} --outfmt 102 --id {params.medianHitLength}')
        else:
            print("Diamond -- Nothing to do here:", {params.runID})

rule areport:
    input: 
        classification = "{PATH}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.classification" # "/mnt/fass2/projects/kirsten/diamond/{sample}_{run}.{tool}.classification"
    output:
       # areport="/mnt/fass2/projects/kirsten/diamond/{sample}_{run}.{tool}.areport"        
        areport="{PATH}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.areport"
    conda:
        "envs/main.yaml"
    params:
        report="{PATH}/result/classification/{tool}/{run}/{sample}_{run}.{tool}.report",
        # report="/mnt/fass2/projects/kirsten/clark_index/{sample}_{run}.{tool}.report",
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
        

