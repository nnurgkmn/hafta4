#!/bin/bash
def donustur(a):
    aout = []  
    for lady in a:
        print(lady)
        sayac = 0
        for harf in lady:   
            sayac += 1
        print(sayac)
        aout.append(sayac)
    
    print('Listeden yazdırma başlıyor')
    return aout  
a = ["nur", "begüm", "irem"]
sonuc = donustur(a)
print(sonuc)