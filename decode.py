from sino import Sinos,Sino
import random
import prime

class Decoder:
	def __init__(self,ss,M,N):
		self.pset = [a.p for a in ss]
		self.maxd = M
		self.sinoList = ss
		self.Big = Sino.synthesize(self.sinoList)
		self.N = N

	def attempt(self):
		if self.Big<self.maxd:
			return "found",self.Big
		else:
			s = set()
			while len(s)<self.N:
				s.add(random.choice(self.pset))
			r = 1L
			for x in s:
				r *= x
			f = self.Big%r
			if f<self.maxd:
				return "found",f
			else:
				return "miss",f

	def do(self,n):
		for i in range(n):
			mesg,f = self.attempt()
			if (i%100)==99:
				print mesg,i
			if mesg=="found":
				print mesg,i
				return f
		return -1L


def main():
	h = random.randint(0,2L**256)
	print h

	p = prime.primeNumber()[-32:]
	R = Sino.repersentation(h,Sino.fromList(p))
	R = Sino.errorList(R,8)
	dec = Decoder(R,2L**256,17)
	# print R
	
	r = dec.do(10000)
	print r==h

if __name__ == '__main__':
	main()
