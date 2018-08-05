def primeNumber():
	r = [2,3,5,7,11,13,17]
	r = findPrime(r,256)
	r = findPrime(r,65536)
	return r

def findPrime(r,N):
	n = len(r)
	for k in range(r[-1],N,2):
		f = True
		for i in range(n):
			if k%r[i]==0:
				f = False
				break
		if f:
			r.append(k)
	return r

def main():
	p = primeNumber()
	m = 1L
	n = len(p)
	r = []
	for i in range(n):
		m = m*p[i]
		if (i-17)>=0:
			m = m/p[i-17]
		if m>2L**256:
			r.append(m)
	print len(p)-len(r),len(r)
	print hex(2L**256)
	for x in r[-10:]:
		print hex(x)

if __name__ == '__main__':
	main()