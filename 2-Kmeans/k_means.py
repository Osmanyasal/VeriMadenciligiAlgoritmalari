import pandas as pd
import math
def k_means(data,numberOfClouster):
    if type(data) == type(pd.DataFrame()):
        
        iterasyon_sayisi = 1
        origins2 = []
        origins = []
        clousters = []
        clouster_temp = []
        
        temp = data.copy()  ## copy of real data
        lenOfUnit = math.ceil(data.shape[0] / numberOfClouster)
         
        for i in range(numberOfClouster):
            clouster_temp.append([])        ## her kume icin bir bosluk aciyoruz ileride kullanicagiz.
        
        ### verilen datayı kumelere ayirir.
        for i in range(numberOfClouster):
            print("kalanlar :",temp.shape[0],lenOfUnit)
            
            if temp.shape[0] >= lenOfUnit:
                clousters.append([temp.iloc[:lenOfUnit]])
            else:
                print("else kisiminda")
                clousters.append([temp.iloc[:]])
                break 
             
            temp = temp.iloc[lenOfUnit:]
        print("clousters sayi ...:",len(clousters))
        print(clousters)
        ##
        
        
        
        ### Kumelere ayrilmis olan verilerin merkezlerini bulur
        while True:
            print("iterasyon :",iterasyon_sayisi,"_"*30)
            iterasyon_sayisi += 1
            total = 0
            top = []
            #print("values.....")
            for i in range(numberOfClouster):   ## clousterin her bir elemani
                for j in range(data.shape[1]):  ##  her bir sutun icin
                    for k in range(len(clousters[i][0])):  ##   her bir satirdan basla
                        #print(clousters[k][j],end = ' ')
                        total += float(clousters[i][0].iloc[k,j])
                    print("total :",total)
                    total = total / (clousters[i][0].shape[0])
                    
                    top.append(total)
                    total = 0
                    
                origins.append(top)
                top = []
            
            print(origins)
            
            del top , total
            ##
            
            ### tum elemanlarin merkez noktalarina olan uzakliklarina
            #   gore yeni kumelerine yerlestirmemiz lazim
            temp = data.copy()  ## verilerin kopyasini aldik
            
            uzaklik = 0
            uzakliklar = []
            kume_index = 0
            for i in range(temp.shape[0]):   ## satirlar 
                for k in range(len(origins)):   # merkez elemanlari kadar 
                    for j in range(temp.shape[1]):  #sutunlar 
                        uzaklik += abs(temp.iloc[i,j] - origins[k][j])
                    uzakliklar.append(uzaklik)
                    uzaklik = 0
                
                kume_index = uzakliklar.index(min(uzakliklar)) 
                print("kumesi ....:",kume_index+1)
                uzakliklar.clear()
                
                ## ilgili elemani ilgili kumeye yerlestirelim
                clouster_temp[kume_index].append(temp.iloc[[i]])  # ilgili satiri yeni kumeye yerlesitirdik.
            
            if  origins == origins2:
                print("algoritma bitti ... !!!")
                return clouster_temp
            else:
                clousters = clouster_temp.copy()
                clouster_temp.clear()
                 
                for i in range(numberOfClouster):
                    clouster_temp.append([])        ## her kume icin bir bosluk aciyoruz ileride kullanicagiz.
                
                print("-"*30)
                print("veriler")
                print(clousters)
                
                origins2 = origins.copy()
                origins.clear()
                
        
    else:
        print("data must be a DataFrame")
        print(type(data),type(pd.DataFrame()))
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
        