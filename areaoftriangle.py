def triangle(base, height) :
    #print ("triangle", base, height)
    a = (base * height) / 2
    return a
b = input("Enter Base:")
h = input("Enter Height:")
fb = float(b)
fh = float(h)

ar = triangle(fb,fh)
print("Area",ar)
