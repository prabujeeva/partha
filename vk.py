N=int(input())
temp = N
arm = 0
while(N!=0):
	rem=N%10
	arm=arm+(rem**3)
	N=N//10
if(temp==arm):
	print("yes")
else:
	print("no")
