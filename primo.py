print("hello world")

print(12*45+54)
import math
from math import sqrt
from math import asin
from math import sin
from math import cos
from math import radians
#print((asin(radians(12471)))*((sqrt(sin(**2))*(0,5)))*(radians(59,9)-(49,3)))+((cos(radians(59,9)))*(cos(radians)(49,3))*(sin(**2))(1)*(atan(2))*(radians(10,8))-(radians (-123,2)))

o1 = radians (59.9)
o2 = radians (49.3)
a1 = radians (10.8)
a2 = radians (-123.1)

cos1 = cos(o1)
cos2 = cos(o2)


d2 = cos1 * cos2 *  sin (0.5 * (a2 - a1))**2
d1 = 2 * 6371 * asin(sqrt (sin(1 / 2 * (o2 - o1))**2 + d2))
print(d1)