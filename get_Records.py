# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:18:18 2019

@author: 764958
"""
import pandas as pd
import numpy as np
import auto_date

#orignal_sheet=pd.read_excel('SVAL Consolidated  with Delta.xlsx',sheet_name='SVAL_Delta_added')
swal_without_sign=pd.read_csv('Records/SVAL_Records/SVAL without sign.txt', sep='\t', lineterminator='\n')
swal_sign=pd.read_csv('Records/SVAL_Records/SVAL Sign.txt', sep='\t', lineterminator='\n')
swal_without_sign=swal_without_sign.merge(swal_sign,on='DataId',how='outer')
swal_without_sign.rename(columns={"DocumentID": "Record_Name"}, inplace=True)

swal_without_sign.drop(["Record_Id","Attr_Status"],axis=1,inplace=True)

swal_without_sign["RecordId"]=swal_without_sign['Record_Name'].apply(lambda x:   x.split(' ',1)[0])
#swal_without_sign["Reviewers&Approvers"]=swal_without_sign['Reviewers&Approvers'].apply(lambda x:  auto_date.datefix(x) )
#swal_without_sign["RecId"]=swal_without_sign["RecId"].str.get(0)

    

swal_without_sign["path"]=np.nan
swal_without_sign["PEPF"]=""
col=list(swal_without_sign.columns.values)
swal_without_sign=swal_without_sign[[col[1],col[2],col[0],col[3],col[7],col[5],col[4],col[8],col[6],col[9]]]

final_set=swal_without_sign[swal_without_sign["DocStatus"]=="Approved"]
col=list(final_set.columns.values)

final_set[col[8]].astype(str)
final_set.fillna('N/A',inplace=True)
final_set.columns = ['ProjId','ProjName','DataId','RecordName','RecordId','Flag','DocStatus','Path','R&A','PEPF']
df_obj = final_set.select_dtypes(['object'])
final_set[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
cout=[]
for temp in final_set.index:
   # print(final_set.at[temp,"R&A"])
    if not(final_set.at[temp,"R&A"]=="N/A"):       
        final_set.at[temp, "R&A"]= auto_date.datefix(final_set.at[temp,"R&A"])

final_set.to_excel("Records/SVAL_Records/Output_Records.xlsx", sheet_name="Main_Sheet", index=False)

       #not "nan"==str(row[col[8]]):
       #final_set.at[index, col[8]] 
       # a.append(auto_date.datefix(str(row[col[8]])))   


#col=list(swal_without_sign.columns.values)


