# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:26:40 2019

@author: 764958
"""

import pandas as pd
import numpy as np
#import auto_date

#swal_manual_1=pd.read_csv('Records/SVAL_Manual_Records/SVAL Manual Records 1.txt', sep='\t', lineterminator='\n')
swal_manual_2=pd.read_csv('Records/SVAL_Manual_Records/SVAL Manual Records 2.txt', sep='\t', lineterminator='\n')
swal_manual_2["Path"]=""
swal_manual_2["R&A"]=""
swal_manual_2["PEPF"]=""

col=list(swal_manual_2.columns.values)

swal_manual_2=swal_manual_2[[col[0],col[1],col[2],col[3],col[5],col[4],col[6],col[7],col[8],col[9]]]
swal_manual_2.columns = ['ProjId','ProjName','DataId','RecordName','RecordId','Flag','DocStatus','Path','R&A','PEPF']

#swal_manual_2=swal_manual_2.merge(swal_manual_1,on='dataid')
swal_manual_2["RecordName"].astype(str)
for temp in swal_manual_2.index:
       
        #str.split(" ",str(swal_manual_2.at[temp,"RecordID"]))
        if not (str.split(str(swal_manual_2.at[temp,"RecordName"]))[0]==""):
            swal_manual_2.at[temp,"RecordId"]=str.split(str(swal_manual_2.at[temp,"RecordName"]))[0]
            
df_obj = swal_manual_2.select_dtypes(['object'])
swal_manual_2[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
swal_manual_2.to_excel("Records/SVAL_Manual_Records/Output_Manual_Records.xlsx", sheet_name="Manual_Records_Sheet", index=False)
#print(str.split(str(swal_manual_2.iloc[323,3]))[0])