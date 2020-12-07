## What did the Benchmark-Paper do?
- calculate norms between vector of classified species and ground truth abundance ürofiles
- create abundance profile vector: each individual species sum is divided by total abundance classified at a given taxonomic rank
- each vector should have normalized magnitude of 1
- generation of 2D matrix of method similarity: compute pairwise distance between species abundace profiles for each classification method
- L2 Distance: euklidic distance
- median L2 distance across benchmarking samples is taken as pairwise similarity for each (m1, m2)-pair
- hierachical clustering wirh Nearest Point on median L2 distances --> scipy

- abundance can be relative abundance of reads from each taxa or inferring abundance of number of individuals from each taxa by correcting read counts for genome size
- abundance profile distance is more sensitive to accurate quantificationn of highly abundant taxa present in sample
- this measure along AUPR allows comprehensive evaluation of performance
  - APS: high numbers of very-low-abundance false positives will not dramatically affectthe measure because they comprise only a small portion of the total abundance
  - AUPR: highle sensitive to classifiers performance in correctly identifying low abundance taxa
- L2 distance can be considered as representation of abundance profile
- other distance to compare abundance profiles: UniFrac --> but complicates because of unknown evolutionary distance
