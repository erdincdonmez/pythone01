import os
def anamenu():
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    #print("║\033[1;31;40m")
    print("║     ETKİN APP       ║") 
    print("╠═════════════════════╣")
    #print("\033[1;32;40m    ║")
    print("║  1-Hesaplamalar     ║")
    print("║  2-Çizimler         ║")
    print("║  3-Oyunlar          ║")
    print("║  5-                 ║")
    print("║  6-                 ║")
    print("║  7-                 ║")
    print("║  8-                 ║")
    print("║  9-                 ║")
    print("║ 10-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()
    #print(secim,"seçildi.")
    if secim =="1":
        #print("Hesap yapmak istiyorsun demek.")
        import moduller.hesapmakinesi        
    if secim =="2": #print("Çizim yapmak istiyorsun demek.")
        os.system('cls')
        import moduller.cizimler
    if secim =="10" : exit()
    #import os
    os.system('cls')
    anamenu()
#print("merhaba")
anamenu()



