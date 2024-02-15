r1 = 30 #cm
r2 = 45 #cm
r3 = 33 #cm

h = 130 #cm

pi = 3.1415

s1 = pi * (r1 **2)
s2 = pi * (r2 **2)
s3 = pi * (r3 **2)
s2m4 = s2 * 4
V = (1 / 6) * h  * (s1 + s2m4 + s3)
VolumeInLitri = ( V / 1000 )
print(VolumeInLitri)  