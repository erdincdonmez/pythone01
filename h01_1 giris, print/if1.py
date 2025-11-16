ad = input('Adın ne?')
print ("Demek adın ", ad)
yil = input(f"Hangi yılda doğdun {ad}?")

yas = 2025-int(yil)

print(f"Demek yaşın {yas}.")

print(yas)

if yas>17 :
    print("Sen ehliyet te alabilirsin.")
else :
    print("Tüh be. 18 olsaydın, ehliyet alabilirdin.")
