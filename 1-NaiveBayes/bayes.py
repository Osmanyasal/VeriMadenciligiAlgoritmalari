# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:40:43 2019

@author: Osman
"""

import pandas as pd
import naive_bayes as bayes

data = pd.read_excel("bayes.xlsx").iloc[:,1:]
tahmin = data.iloc[9:,0:3]
data = data.iloc[:-2,:]

bayes.naive_bayes(data,tahmin)


