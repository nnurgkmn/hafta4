def donustur(a):
    aout = []  
    for lady in a:
        #print(lady)
        sayac = 0
        for harf in lady:   
            sayac += 1
        #print(sayac)
        aout.append(sayac)
    
    print('Listeden yazdırma başlıyor')
    return aout  




g = "steğe bağlı tanımlama bilgilerini, sosyal medya bağlantıları gibi web sitelerimizde deneyiminizi iyileştirmek ve çevrimiçi etkinliğinize dayalı olarak kişiselleştirilmiş reklamlar görüntülemek için kullanırız. İsteğe bağlı tanımlama bilgilerini reddederseniz yalnızca size hizmetleri sağlamak için gerekli tanımlama bilgileri kullanılır. Sayfanın altındaki 'Tanımlama Bilgilerini Yönet' bağlantısına tıklayarak seçiminizi değiştirebilirsiniz"

kelimeler=g.split(" ")
sonuc = donustur(kelimeler)
print(sonuc)
