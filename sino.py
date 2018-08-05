import random
from gcd import exGCD

class Sino:
	def __init__(self,p):
		self.p = p
		self.r = 0
	def put(self,a):
		self.r = a%self.p
		return self
	@staticmethod
	def fromList(p):
		return [Sino(pi) for pi in p]

	@staticmethod
	def repersentation(A,p):
		return [s.put(A) for s in p]

	@staticmethod
	def merge(a,b):
		(d,r,l) = exGCD(a.p,b.p)
		if d!=1:
			p = b.p/d
			return Sino.merge(a,Sino(p).put(b.r))
		else:
			p = a.p*b.p
			r = (a.r*l*b.p+b.r*r*a.p)
			return Sino(p).put(r)
	
	@staticmethod	
	def synthesize(R):
		if len(R)==1:
			return R[0].r
		else:
			return Sino.synthesize([Sino.merge(R[0],R[1])]+R[2:])
	
	def __repr__(self):
		return str(self.r)+'|'+str(self.p)
	
	@staticmethod
	def find(R,p):
		for a in R:
			if a.p==p:
				return a
		return None

	@staticmethod
	def delete(R,p):
		nR = []
		for a in R:
			if a.p!=p:
				nR.append(a)
		return nR

	@staticmethod
	def error(R,p,r):
		nR = []
		for a in R:
			if a.p == p:
				a.r = r
			nR.append(a)
		return nR

	@staticmethod
	def Product(R):
		r = 1L
		for a in R:
			r *= a.p
		return r

	@staticmethod
	def errorList(R,n):
		p = []
		for s in R:
			p.append(s.p)
		for i in range(n):
			pi = random.choice(p)
			R = Sino.error(R,pi,random.randint(0,pi-1))
			print "add error",pi
		return R

class Sino2(Sino):
	def __init__(self,p0,p1):
		self.p0 = p0
		self.p1 = p1
		Sino.__init__(self,p0*p1)

	def check(self,a):
		(d,r,l) = exGCD(a.p,self.p)
		if d==1:
			return None
		else:
			if self.r%d != a.r%d:
				return None
			else:
				return Sino(d).put(self.r)
	
	@staticmethod
	def fromList(p):
		return [Sino2(p0,p1) for (p0,p1) in zip(p,p[1:]+p[-1:])]
	
	@staticmethod
	def checkList(R):
		r = []
		for i in range(len(R)-1):
			a = R[i].check(R[i+1])
			if a!=None:
				r.append(a)
		a = R[-1].check(R[0])
		if a!=None:
			r.append(a)
		return r	

def main():
	import random
	from prime import primeNumber
	p = [15,21]
	A = 33
	r = Sino.repersentation(A,Sino.fromList(p))
	print r
	R = Sino.merge(r[0],r[1])
	print R
	A = random.randint(0,2L**256)
	print A
	p = primeNumber()[-32:]
	r = Sino.repersentation(A,Sino.fromList(p))
	print r
	R = Sino.synthesize(r)
	print R
	print Sino.find(r,p[-1])
	r = Sino.repersentation(A,Sino2.fromList(p))
	print r
	R = Sino.synthesize(r)
	print R
	

if __name__ == '__main__':
	main()