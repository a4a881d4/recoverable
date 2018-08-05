

"""
LL ex_gcd(LL a,LL b,LL &x,LL &y)
{
    LL d = a;
    if(!b){x = 1,y = 0;}
    else{
      d = ex_gcd(b,a%b,y,x);
      y-=a/b*x;
    }
    return d;
}
"""

def exGCD(a,b,x=1,y=0):
	d = a
	if b==0:
		x = 1
		y = 0
	else:
		(d,y,x) = exGCD(b,a%b,y,x)
		y = y-a/b*x
	return (d,x,y)

def inv(a,b):
	(d,r,l)=exGCD(a,b)
	return r

def invList(a,n):
	r = [inv(n,x) for x in a]
	return r

def testGCD():
	import random
	A = random.randint(0,2L**32)
	B = random.randint(0,2L**32)
	(d,x,y) = exGCD(A,B)
	print A,B,d,A%d,B%d,x,y
	print x*A+y*B

if __name__ == '__main__':
	testGCD()