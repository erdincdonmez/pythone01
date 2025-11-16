print("╔═════════════════════╗")
print("║     HESAPLAMALAR    ║") 
print("╠═════════════════════╣")
print("║  1-Hesap makinesi   ║")
print("║  2-Kare alan hesabı ║")
print("║  3-Kare çevre hesabı║")
print("║  5-Üst alma         ║")
print("║  6-                 ║")
print("║  7-                 ║")
print("║  8-Anamenu          ║")
print("║  9-Çıkış            ║")
print("║                     ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")
scm=input()
if scm=="1": pass
elif scm=="2": import moduller.hsp_karea
elif scm=="3": import moduller.hsp_karec
else: exit()
