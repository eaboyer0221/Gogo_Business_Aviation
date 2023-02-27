"""
python script to concatenate csv files
"""
import os
import glob
import pandas
 
def concatenate (indir="W:\\BA_CustOps_Data_Analytics\\SCE_for_Emily\\extracted2",outfile="W:\\BA_CustOps_Data_Analytics\\SCE_for_Emily\\concatenated2.csv"):
    os.chdir(indir)
    fileList=glob.glob("*.csv")
    #create empty list object
    dfList=[]
    #iterate through file list
    for filename in fileList:
	print(filename)
	#generate data frame from file
	df=pandas.read_csv(filename,header=None)
	#append data frame to empty list
	dfList.append(df)
    concatDf=pandas.concat(dfList,axis=0)#concatenate vertically
    #export df to csv
    concatDf.to_csv(outfile,index=None)
