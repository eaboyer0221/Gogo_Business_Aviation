"""
python script that iterates through directories and unzips the csv.gz files within to .csv

"""

import gzip
import time
import os
from os.path import join

for (dirname, dirs, files) in os.walk(r'W:/BA_CustOps_Data_Analytics/SCE_Multiple_Days/'):
   for filename in files:
       print (dirname,filename)
       if filename.endswith('.gz') :
           thefile = os.path.join(dirname,filename)
           size = os.path.getsize(thefile)
           if filename.endswith('.gz') :
               starttime=time.time()
               print(r'%s/%s' %(dirname,filename))
               with gzip.open('%s/%s' %(dirname,filename), 'r') as my_gz:
                   print ('Y:\\sce\\%s' %filename[:-3])
                   file_content = my_gz.read()
                   with open('Y:\\sce\\%s' %filename[:-3], 'wb') as my_csv:
                       my_csv.write(file_content)
                       endtime=time.time()
                       runtime=endtime-starttime
                       print runtime     
