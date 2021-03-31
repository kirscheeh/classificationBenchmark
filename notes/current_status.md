# Abundances Species, gridion364
|            	| B. subtilis 	| L. monocytogenes 	| E. faecalis 	| S. aureus 	| S. enterica 	| E. coli 	| P. aeruginosa 	| L. fermentum 	| S. cerevisiae 	| C. neoformans 	| total   	|   AUPR	|   Abundance Similarity Profile	|   	|
|------------	|-------------	|------------------	|-------------	|-----------	|-------------	|---------	|---------------	|--------------	|---------------	|---------------	|---------	|---	|---	|---	|
| 'truth'| 0.193| 0.1456| 0.1224| 0.1128| 0.0999| 0.0993| 0.097| 0.0928| 0.0192| 0.0178|0.9998|1|0||
| ccmetagen  	| 0.00357     	| 0.113            	| 0.0179      	| 0.0984    	| -           	| 0.021   	| 0.0339        	| -            	| 0.00894       	| 1.14e-06     	| 0,2967  	|   0.6260912698412698	|   0.0773	|   	|
| clark      	| 0.073       	| 0.1324           	| 0.1144      	| 0.1121    	| 0.0565      	| 0.0496  	| 0.0456        	| -            	| -             	| -             	| 0,5836  	|   0.754591836734694	|   0.0309	|   	|
| centrifuge 	| 0.18        	| 0.1327           	| 0.1097      	| 0.1104    	| 0.0589      	| 0.0582  	| 0.05115       	| 0.1425       	| -             	| -             	| 0,84355 	|   1	|   0.00912	|   	|
| diamond    	| 0.0039      	| 0.029            	| 0.0101      	| 0.004     	| 0.0026      	| 0.00115 	| 0.00104       	| -            	| -             	|               	| 0,05179 	|   0.754591836734694	|   0.1115	|   	|
| kaiju      	| 0.00811     	| 0.093            	| 0.1027      	| 0.042     	| 0.0178      	| 0.0212  	| 0.01103       	| 0.125        	| -             	| -             	| 0,42084 	|   0.6427579365079366	|   0.06442	|   	|
| kraken2    	| 0.175       	| 0.1287           	| 0.1111      	| 0.111     	| 0.0569      	| 0.0525  	| 0.04481       	| 0.1414       	| 0.0217        	| 0.02          	| 0,86311 	|   0.7048336033752737	|   0.009883	|   	|
|kslam|läuft|noch|||||||||||||
<!-- |expected truth|0.12|0.12|0.12|0.12|0.12|0.12|0.12|0.12|0.02|0.02|1.0|1.0|0.0|-->
- APS: average precision score --> AUPR
![](pics/gridion364.barplot.png)
# Precision Recall Curves + Pie Charts, gridion364
| PR Curve <br> (eigenes Skript) | PR curve <br> (sklearn)| Pie Chart Species-Lvl <br> (Abundance>=1%) |
|:---:|:---:|:---:|
|![](pics/gridion364_default.ccmetagen.png)|![](pics/gridion364_default.ccmetagen.sklearn.png)|![](pics/gridion364_default.ccmetagen.piechart.png)|
|![](pics/gridion364_default.clark.png)|![](pics/gridion364_default.clark.sklearn.png)|![](pics/gridion364_default.clark.piechart.png)|
|![](pics/gridion364_default.centrifuge.png)|![](pics/gridion364_default.centrifuge.sklearn.png)|![](pics/gridion364_default.centrifuge.piechart.png)|
|![](pics/gridion364_default.diamond.png)|![](pics/gridion364_default.diamond.sklearn.png)|![](pics/gridion364_default.diamond.piechart.png)|
|![](pics/gridion364_default.kaiju.png)|![](pics/gridion364_default.kaiju.sklearn.png)|![](pics/gridion364_default.kaiju.piechart.png)|
|![](pics/gridion364_default.kraken2.png)|![](pics/gridion364_default.kraken2.sklearn.png)|![](pics/gridion364_default.kraken2.piechart.png)|
|||

- Threshold steps: 0.001
 - ccmetagen hat html-output, auf die Zahlen komm ich noch nicht

# Abundances Species, gridion366
|            	| B. subtilis 	| L. monocytogenes 	| E. faecalis 	| S. aureus 	| S. enterica 	| E. coli 	| P. aeruginosa 	| L. fermentum 	| S. cerevisiae 	| C. neoformans 	| total   	|   AUPR	|   Abundance Similarity Profile	|   	|
|------------	|-------------	|------------------	|-------------	|-----------	|-------------	|---------	|---------------	|--------------	|---------------	|---------------	|---------	|---	|---	|---	|
| ccmetagen  	|   0.00024   	|      0.76197       	|    0   	|  0   	| 0           	|    8.718e-07	|   0.03007      	|        0    	|       0.002  	|    0 	|   0.7943	|   0.79333	|  	|   	|
| clark      	|       	|           	|     	|     	|       	|  	|         	|            	|              	|              	|   	|   	|   	|   	|
| centrifuge 	| 0.0107        	| 0.836           	| 0.0003      	| 1.922e-05   	| 0.00054      	| 0.000604  	| 0.04599       	| 5.174e-05       	| -             	| -             	| 0.89429 	|   0.61937	|   	|   	|
| diamond    	|       	|             	|       	|      	|       	|  	|        	| -            	| -             	|               	|  	|   	|   	|   	|
| kaiju      	| 0.0005     	| 0.579            	| 0.0001      	| 4.008e-05     	| 0.000155      	| 0.00018  	| 0.00971       	| 4.308e-05        	| -             	| -             	| 0.58978 	|   0.41206	|   	|   	|
| kraken2    	| 0.01027       	| 0.8129           	| 0.0016      	| 3.79e-05     	| 0.00048      	| 0.00048  	| 0.0398       	| 5.15e-05     | 0.0069        	| 2.699e-05          	| 0.87261 	|   0.26045	|   	|   	|
|kslam|läuft|noch|||||||||||||
- hier keine Verteilung bekannt wie bei 364 --> Species sind log-verteilt, L. monocytogenes mitknapp 89% am meisten, S. cerevisiae mit unter 0.0009% am wenigsten
![](pics/gridion366.barplot.png)
# Precision Recall Curves + Pie Charts, gridion366
| PR Curve <br> (eigenes Skript) | PR curve <br> (sklearn)| Pie Chart Species-Lvl <br> (Abundance>=1%) |
|:---:|:---:|:---:|
|![](pics/gridion366_default.ccmetagen.png)|![](pics/gridion366_default.ccmetagen.sklearn.png)|![](pics/gridion366_default.ccmetagen.piechart.png)|
|![](pics/gridion366_default.clark.png)|![](pics/gridion366_default.clark.sklearn.png)|![](pics/gridion366_default.clark.piechart.png)|
|![](pics/gridion366_default.centrifuge.png)|![](pics/gridion366_default.centrifuge.sklearn.png)|![](pics/gridion366_default.centrifuge.piechart.png)|
|![](pics/gridion366_default.diamond.png)|![](pics/gridion366_default.diamond.sklearn.png)|![](pics/gridion366_default.diamond.piechart.png)|
|![](pics/gridion366_default.kaiju.png)|![](pics/gridion366_default.kaiju.sklearn.png)|![](pics/gridion366_default.kaiju.piechart.png)|
|![](pics/gridion366_default.kraken2.png)|![](pics/gridion366_default.kraken2.sklearn.png)|![](pics/gridion366_default.kraken2.piechart.png)|
|||


# Laufzeiten
|            	| kma            	| ccmetagen      	| clark                 	| centrifuge     	| kaiju          	| kraken2        	| diamond                 	| kslam 	|
|------------	|----------------	|----------------	|-----------------------	|----------------	|----------------	|----------------	|-------------------------	|-------	|
| gridion364 	| 0:58:33.332763 	| 0:00:19.790294 	| 1 day, 7:02:37.059451 	| 3:28:34.545058 	| 3:30:55.818875 	| 0:08:55.109309 	|                         	|       	|
| gridion366 	| 2:03:00.949100 	| 0:00:12.93     	|                       	| 4:45:25.614299 	| 3:40:21.257391 	| 0:11:17.788488 	| 4 days, 10:02:19.511836 	|       	|
|            	|                	|                	|                       	|                	|                	|                	|                         	|       	|


# Tools that don't work
## MetaOthello

    start to fix reads in phase1, turn: 1
    /bin/bash: line 1: 50673 Segmentation fault

## taxMaps
    txM.gridion364_default.taxmaps.classification.sh: line 19: 20678 Done(1) cat txM.gridion364_default.taxmaps.classification.map/gridion364_default.taxmaps.classification.filtout.map txM.gri$
        20679 | txM_lca -t txM.gridion364_default.taxmaps.classification.base/taxonomy.tbl.gz -m s 2> txM.gridion364_default.taxmaps.classification.map/gridion364_default.taxmaps.classi$
        20680 Bus error

