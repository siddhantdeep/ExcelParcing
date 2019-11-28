# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 00:19:27 2019
=RIGHT(A5576,LEN(A5576)-FIND("-",A5576))
@author: 764958
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_excel('CLDMS_DA_Preload_Metadata_Prod.xlsx','Sheet5')
dataset.fillna('N/A',inplace=True)
for temp in dataset.index:
   # print(final_set.at[temp,"R&A"])
    if(dataset.at[temp,"Short"]=="N/A"):       
        dataset.at[temp, "Short"]= dataset.at[temp,"Section"]
dataset.to_excel("DA Section Mapping.xlsx",index = None, header=True)