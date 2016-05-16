#QUICK USE  

##Environment  

* Linux OS
* Python >= 2.7
* jdk >= 7 (for java spider)
* Python Modules: sickit-learn(python-sklearn), numpy, and some common modules.  

##Use
###report format  
`$ python detector.py -d -q -f filepath`  

###json format
`$ python detector.py -d -q -j -f filepath`  

###full format (with full log)
`$ python detector.py -d -f filepath`

##Example
###report format
`$ python detector.py -d -q -f filepath`

>#################
\# Detect Report #
#################
[Control Power]
24.54
[Class]
Low
[Dangerous Permissions]
android.permission.READ_PHONE_STATE
[All Permissions]
miui.permission.USE_INTERNAL_GENERAL_API
android.permission.READ_EXTERNAL_STORAGE
android.permission.WRITE_EXTERNAL_STORAGE
android.permission.INTERNET
android.permission.WRITE_SETTINGS
android.permission.ACCESS_NETWORK_STATE
android.permission.ACCESS_WIFI_STATE
android.permission.READ_PHONE_STATE
android.permission.GET_TASKS
android.permission.VIBRATE
com.android.launcher.permission.WRITE_SETTINGS
com.android.launcher.permission.READ_SETTINGS
com.mfashiongallery.emag.permission.MIPUSH_RECEIVE

###json format
` $python detector.py -d -q -j -f filepath`

>{"Dangerous Permissions": ["android.permission.READ_PHONE_STATE"], "All Permissions": ["miui.permission.USE_INTERNAL_GENERAL_API", "android.permission.READ_EXTERNAL_STORAGE", "android.permission.WRITE_EXTERNAL_STORAGE", "android.permission.INTERNET", "android.permission.WRITE_SETTINGS", "android.permission.ACCESS_NETWORK_STATE", "android.permission.ACCESS_WIFI_STATE", "android.permission.READ_PHONE_STATE", "android.permission.GET_TASKS", "android.permission.VIBRATE", "com.android.launcher.permission.WRITE_SETTINGS", "com.android.launcher.permission.READ_SETTINGS", "com.mfashiongallery.emag.permission.MIPUSH_RECEIVE"], "Control Power": "24.54", "Class": "Low"}

###full format (with full log)
`$ python detector.py -d -f filepath`

>################################################################
\#  Welcome to use Android Permission Detector(Version 1.0.2)!  #
################################################################

>[INFO] asctime detector.py commandLine: Detect start.

>[INFO] asctime detector.py commandLine: Detect finish.

>[INFO] asctime detector.py commandLine: result: ('24.54', [u'android.permission.READ_PHONE_STATE'], [u'miui.permission.USE_INTERNAL_GENERAL_API', u'android.permission.READ_EXTERNAL_STORAGE', u'android.permission.WRITE_EXTERNAL_STORAGE', u'android.permission.INTERNET', u'android.permission.WRITE_SETTINGS', u'android.permission.ACCESS_NETWORK_STATE', u'android.permission.ACCESS_WIFI_STATE', u'android.permission.READ_PHONE_STATE', u'android.permission.GET_TASKS', u'android.permission.VIBRATE', u'com.android.launcher.permission.WRITE_SETTINGS', u'com.android.launcher.permission.READ_SETTINGS', u'com.mfashiongallery.emag.permission.MIPUSH_RECEIVE'])

>#################
\# Detect Report #
#################
[Control Power]
24.54
[Class]
Low
[Dangerous Permissions]
android.permission.READ_PHONE_STATE
[All Permissions]
miui.permission.USE_INTERNAL_GENERAL_API
android.permission.READ_EXTERNAL_STORAGE
android.permission.WRITE_EXTERNAL_STORAGE
android.permission.INTERNET
android.permission.WRITE_SETTINGS
android.permission.ACCESS_NETWORK_STATE
android.permission.ACCESS_WIFI_STATE
android.permission.READ_PHONE_STATE
android.permission.GET_TASKS
android.permission.VIBRATE
com.android.launcher.permission.WRITE_SETTINGS
com.android.launcher.permission.READ_SETTINGS
com.mfashiongallery.emag.permission.MIPUSH_RECEIVE

###Detect Error
`$ python detector.py -d -q -f filepath`
>[ERROR] asctime mainMachineLearning.py test: Test abort
