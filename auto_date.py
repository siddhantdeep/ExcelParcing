# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:17:34 2019

@author: 764958
"""
import re
from datetime import *
def datefix(s):
    
    
   # s = 'Kirsten Timmermann~16/10/2017 08:21:01;Betina Schepers~19/10/2017 19:31:55;Yuxin Rao~01/11/2017 04:43:47;Karolina Dabrowska~05/12/2017 19:06:42;Kim Dashen~06/11/2017 23:54:04;Denise Stearns~09/11/2017 18:37:00;Deborah Thurston~24/10/2017 22:21:59;Robert Marshall~27/10/2017 10:23:42;Elizabeth Rehfeld~30/10/2017 13:40:11;Kirsten Timmermann~06/12/2017 08:20:57;George Galinski~13/12/2017 22:02:48;Kim Dashen~14/12/2017 17:12:12;Betina Schepers~11/12/2017 07:44:47;Karolina Dabrowska~10/01/2018 00:12:23;Deborah Thurston~08/12/2017 13:10:03;Denise Stearns~12/12/2017 15:48:26;Elizabeth Rehfeld~05/12/2017 21:20:06;Yuxin Rao~10/01/2018 19:47:37;'
   if s: 
       lis=s.split(';')
       data=[]
       if len(lis)>10:
           for temp in lis:
               
              if not temp.isspace():
                  # print(temp)
                   a=re.findall('(?<=~).*', str(temp))#[0].split(" ")
                   #d=a[0].split('/')
                   #d=date(int(d[2]),int(d[1]),int(d[0]))
                   #a[0]=d
                   a.append(re.findall('.*(?=~)',str(temp))[0])
                   
                #   print(temp)
                   data.append(a)
               
           sor= sorted(data,key=lambda x: datetime.strptime(x[0], "%d/%m/%Y %H:%M:%S"),reverse=True)
           r_a=''
           
           for i in range(10):
                  r_a=r_a+sor[i][1]+'~'+sor[i][0]+';'
           return r_a   
           
       else:
           return s
       
   
#print(datefix("Robert Stevenson~16/12/2016 12:23:28;Jurn Wingelaar~22/11/2016 07:59:22;Betina Schepers~21/11/2016 15:43:19;Deborah Thurston~22/11/2016 20:32:50;Sharon Downs~28/11/2016 16:05:13;Teresa Schmidt~17/11/2016 18:04:15;Robert Marshall~14/03/2017 12:30:46;Denise Stearns~24/03/2017 14:02:09;Deborah Thurston~10/03/2017 14:57:50;Teresa Schmidt~27/03/2017 19:56:53;Betina Schepers~10/03/2017 08:00:26;Yuxin Rao~21/02/2017 15:00:22;"))  
     
    
#result = re.search('asdf=5;(.*)123jasd', s)
#print(result.group(1))