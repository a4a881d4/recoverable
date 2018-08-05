import prime
import random

def down(h,p,r):
	rn = r[-1]
	pn = p[-1]
	h -= rn
	h /= pn
	n = prime.invList(p[:-1],pn)
	for m in range(len(r)-1):
		r[m]=(r[m]-rn)*n[m]%p[m]
		if h%p[m]!=r[m]:
			print m,r[m],p[m]
	return h,p[:-1],r[:-1]

p = prime.primeNumber()[-32:]

h = random.randint(0,2L**256)
print h

R = prime.sinoRepersentation(h,p)
print R


"""
s = p[-32:]

r = [h%k for k in s]
r[22]=r[22]+6
for m in range(20):
	(h,s,r) = down(h,s,r)

	print h
	print r

(kn,rn) = s[-1]
h = h - rn
print h
r0 = []

for (k,r) in s:
	(d,n,l) = prime.exGCD(kn,k)
	print (kn*n)%k
	r0.append((k,r,((r-rn)*n)%k,(h/kn)%k))

print r0
"""



