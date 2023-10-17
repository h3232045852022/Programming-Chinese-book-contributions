import gmpy2

p = input("P?")
q = input("q?")
e = input("e?")

s = (p-1)*(q-1)
d = gmpy2.invert(e,s)
print('flag is :',d)