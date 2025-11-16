
# f, format ve %
ad = input('Adın ne?')
print ("Demek adın ", ad)

#yil = input(f"Hangi yılda doğdun {ad}?")
#yil = input("Hangi yılda doğdun {}?".format(ad))
yil = input(f"Hangi yılda doğdun %s?" %(ad))

#print(f"Demek {2025-int(yil)} yaşındasın {ad}.")
print("Demek {} yaşındasın {}.".format(2025-int(yil),ad))
#print(f"Demek %d yaşındasın %s." %(2025-int(yil),ad))

# %d, %s, %f 
