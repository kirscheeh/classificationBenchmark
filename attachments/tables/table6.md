|                	| Diamond   	| Kaiju     	| CCMetagen 	| Centrifuge 	| CLARK     	| Kraken2   	| BugSeq    |
|----------------	|-----------	|-----------	|-----------	|------------	|-----------	|-----------	|-----------|
| GridION364    	| 1.0       	| 0.7253469 	| 0.6887791 	| 1.0        	| 1.0       	| 1.0       	|1.0|
| PromethION365 	|       -    	| 0.7253469 	|       -    	| 1.0        	| 1.0 	      | 1.0       	|-|
| GridION366    	| 0.5103104 	| 0.3873827 	| 0.7760189 	| 0.6062113  	| 0.6914607 	| 0.6724297 	|0.9588289
| PromethION367 	|       -    	| 0.3896924  	|      -     	| 0.6138137  	| 0.7315841 	| 0.6965986 	|-|

***Table 6: AUPR values, Default Database.*** This table shows the calculated AUPR for the different tools and samples using their default database. Note that CCMetagen and Diamond are not able to perform on the PromethION samples, therefore those values are missing. There is no trend to be observed regarding the AUPR and different sequencing depths. However, some tools seem to perform better with the CS Even samples (e.g. Diamond, Centrifuge, Kraken2), whereas Kaiju, CCMetagen and CLARK seem to perform better with the CS Log samples. The corresponding plots can be seen in [***Figure-S9***](../supplements/figure_s9.md "Supplements, Figure 9") or [here](../../stats/pics/prc "Folder of Precision-Recall-Curves"). <br> <br>