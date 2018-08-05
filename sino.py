from gcd import exGCD

class Sino:
	def __init__(self,p,r):
		self.p = p
		self.r = r
	@staticmethod
	def repersentation(A,p):
		return [Sino(pi,A%pi) for pi in p]
	@staticmethod
	def merge(a,b):
		(d,r,l) = exGCD(a.p,b.p)
		if d!=1:
			print "no co"
			p = b.p/d
			return Sino.merge(a,Sino(p,b.r%p))
		else:
			p = a.p*b.p
			r = (a.r*l*b.p+b.r*r*a.p)%p
			return Sino(p,r)
	@staticmethod	
	def synthesize(R):
		if len(R)==1:
			return R
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


	

def main():
	import random
	from prime import primeNumber
	p = [15,21]
	A = 33
	r = Sino.repersentation(A,p)
	print r
	R = Sino.merge(r[0],r[1])
	print R
	A = random.randint(0,2L**256)
	print A
	p = primeNumber()[-32:]
	r = Sino.repersentation(A,p)
	print r
	R = Sino.synthesize(r)
	print R
	print Sino.find(r,p[-1])

if __name__ == '__main__':
	main()