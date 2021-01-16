import getting as get

# mioght not work because either phred33 nor phred64

f = "/home/kirscheeh//university/projectCLASSIFICATION/classificationBenchmark/testingScripts/test.fastq"
qualSeq = get.get_qualityStrings(f)
seq = get.get_sequences(f)
qual = get.get_quality(f, True)
print(len(seq))
#print(seq, qualSeq)
print(qual)