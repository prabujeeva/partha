v,x=map(int,input().split())
for num in range(v+1,x):
 sum=0
 temp=num
 while temp>0:
  g=temp%10
  sum+=g**3
  temp//=10 
 if(num==sum):
  print(num)
