# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:19:57 2019

@author: 764958
"""

import pandas as pd
import numpy as np

new_sheet=pd.read_excel("Records/Records with Duplicates.xlsx", sheet_name="Full_Sheet_with_Dups", index=False)
orignal_sheet=pd.read_excel('SVAL Consolidated  with Delta.xlsx',sheet_name='SVAL_Delta_added')
