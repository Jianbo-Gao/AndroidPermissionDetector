# AndroidPermissionDetecter
Detect an Android application based on permissions.

## Environment
* Linux OS
* Python >= 2.7
* jdk >= 7 (for java spider)
* Python Modules: sickit-learn(python-sklearn), numpy, and some common modules.

## Quick Start
1. Change Directory.
`$ cd ${path}/AndroidPermissionDetecter/`  

2. Check Modules.  
`$ python detecter.py -c`  

3. See Help.  
`$ python detecter.py -h`  

### Train
`$ python detecter.py -t -g GOOGLEDIRPATH -m MALWAREDIRPATH`  

If you wanna save params(-p):  
`$ python detecter.py -t -g GOOGLEDIRPATH -m MALWAREDIRPATH -p PARAMNAME`  

If you do not wanna see log(-q):  
`$ python detecter.py -t -g GOOGLEDIRPATH -m MALWAREDIRPATH -q`  

### Detect
`$ python detecter.py -d -f FILEPATH`  

If you wanna use your own params(-p):  
`$ python detecter.py -d -f FILEPATH -p PARAMNAME`  

If you do not wanna see log(-q):
`$ python detecter.py -d -f FILEPATH -q`  

### Spider
See Help(Simplified Chinese).  
`$ java -jar apkSpider.jar -h`  

Params:  

* -m [yingyongbao|wandoujia|360|baidu|android]: Specify Market(s)  
* -n num: Specify number of each market
* -s: Store apk files 

### API
Simple Result.  
`$ python api.py FILEPATH`  

Response Format:  
`{"score":v1, "degree":v2}`  
v1 is float type: [0,100), %.2f  
v2 is string type: "0"|"1"|"2", means the Control Power of this Android application is low, middle, high.  

## Directory Structure
AndroidPermissionDetecter  
\-\-detecter.py  
\-\-api.py  
\-\-apkSpider.jar  
\-\-src/  
\-\-param/  
\-\-log/  
\-\-logs/  
\-\-data/

* Main functions are in src/  
* Trained models are in param/
* Detecter's log files are in log/
* Spider's log files are in logs/
* Spider's results are in data/


## Samples
Default Model is trained with Tencent Malicious Samples, Rising Malicious Samples and Google Play Benign Samples.