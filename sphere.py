import math
def sphere(radius) :
    v = 4/3 * math.pi * (radius**3)
    return v
r = input("Enter Radius:")
fr = float(r)

ra = sphere(fr)
print("Volume",ra)
