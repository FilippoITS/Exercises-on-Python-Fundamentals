r1 = int(input("RaggioN1: ")) #30cm
r2 = int(input("RaggioN2: ")) #45cm
r3 = int(input("RaggioN3: ")) #33cm

h = int(input("altezza: ")) #130cm

pi = 3.1415

s1 = pi * (r1 **2)

s2 = pi * (r2 **2)
s3 = pi * (r3 **2)
s2m4 = s2 * 4

V = (1 / 6) * h  * (s1 + s2m4 + s3)
Vl = ( V / 1000 )
print("VolumeInLitri: " +str (Vl))  #in litri

r1s = r1**2
r2s = r2**2
r1pr2 = r1 * r2

Abotte = ((r1s + r2s + r1pr2) * pi) + (r1 + r2) * h
print("AreaBotte: " +str (Abotte)) 


