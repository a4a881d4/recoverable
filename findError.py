import prime
import random
from sino import Sino,Sino2
from log import log2


p = prime.primeNumber()[-32:]

h = random.randint(0,2L**256)
print h

R = Sino.repersentation(h,Sino.fromList(p))
print R

eR = Sino.error(R,p[0],1)
eR = Sino.error(eR,p[1],4)

eh = Sino.synthesize(eR)

ieh = eh*p[0]
geh = ieh%Sino.Product(eR)
sgeh = geh/(p[0])
print "eh",log2(eh),eh
print "ieh",log2(ieh),ieh
print "geh",log2(geh),geh
print "sgeh",log2(sgeh),sgeh
s = Sino.Product(eR)%eh
print Sino.Product(eR)/eh
print "s",log2(s),s
print ""

pp = Sino.Product(eR)

for pi in p:
	ps = pp/pi
	ss = eh%ps
	print pi,log2(ss),ss

ps = pp/(p[0])
ss = eh%ps
print log2(ss)

ps = ps/(p[1])
ss = ss%ps
print log2(ss)

R = Sino.repersentation(h,Sino2.fromList(p))
print R
R = Sino.errorList(R,8)
R = Sino2.checkList(R)
h2 = Sino.synthesize(R)

print h2
"""
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



