# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 16:40:49 2019

@author: Osman
"""


import pandas as pd
import naive_bayes as bayes

data = pd.read_excel("sinifOrnegi.xlsx")
tahmin = data.iloc[15:,:-1]
data = data.iloc[:14,:]

bayes.naive_bayes(data,tahmin)

