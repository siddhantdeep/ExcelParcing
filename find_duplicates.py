# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:54:05 2019

@author: 764958
"""

import pandas as pd
import numpy as np


def find_dupes(frames):
    frames.fillna('N/A',inplace=True)
    df_obj = frames.select_dtypes(['object'])
    frames[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    frames[frames.duplicated(['RecordId','Flag'])]

        
    
    
    return frames  
    
swal_manual=pd.read_excel("Records/SVAL_Manual_Records/Output_Manual_Records.xlsx", sheet_name="Manual_Records_Sheet", index=False)
swal_rec=pd.read_excel("Records/SVAL_Records/Output_Records.xlsx", sheet_name="Main_Sheet", index=False)

swal_manual["DocStatus"].astype(str)
swal_manual["DocStatus"]=swal_manual["DocStatus"].str.strip()

swal_manual=swal_manual[(swal_manual["DocStatus"]=="Approved") | (swal_manual["DocStatus"]=="Draft")]

swal_rec=swal_rec.append(swal_manual, ignore_index = True)
duplicates=find_dupes(swal_rec)
duplicates.to_excel("Records/Only_Dupes.xlsx", sheet_name="Only_Dupes", index=False)
swal_rec.to_excel("Records/Records with Duplicates.xlsx", sheet_name="Full_Sheet_with_Dups", index=False)