# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:46:07 2019

@author: Osman
"""
 
def naive_bayes(data , tahmin):
    
    ## kategorileri belirle
    kategoriler = {}
    tamin_kategorileri = {}
    sonuclar = []
    for i in range(tahmin.shape[1]):
        if tahmin.iloc[0,i] not in tamin_kategorileri:
            tamin_kategorileri[str(tahmin.iloc[0,i])] = 0
    
    for i in range(data.shape[0]):
        if data.iloc[i,-1] not in kategoriler:
            kategoriler[str(data.iloc[i,-1])] = 1
        else:
            kategoriler[str(data.iloc[i,-1])] += 1
            
    for j in kategoriler.keys():
        print("j degeri...: ",j)
        for i in range(data.shape[0]):
            if data.iloc[i,-1] == j:
                
                for p in range(tahmin.shape[1]):
                    if str(tahmin.iloc[0,p]) == str(data.iloc[i,p]):
                        tamin_kategorileri[str(tahmin.iloc[0,p])] += 1
                         
        
        print(tamin_kategorileri)
        ## sıra geldi oranlarini hesaplamakta
        tahmin_total = 1
        
        for m in tamin_kategorileri.values():
            print("degerler : ",m,kategoriler[j])
            tahmin_total *= m / kategoriler[j]
            
        tahmin_total = tahmin_total * kategoriler[j] / data.shape[0]
        sonuclar.append(tahmin_total)
        print(sonuclar)
        
        for i in tamin_kategorileri.keys():
            tamin_kategorileri[i] = 0
        
    print(tamin_kategorileri)
    print(kategoriler)
    print("\n**********************\nSonuc degerleri ...: "+str(sonuclar))
    
    
    
    
    
    
    
    
    