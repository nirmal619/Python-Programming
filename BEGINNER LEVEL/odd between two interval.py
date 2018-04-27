k=[]
n,m=input().split()
a=int(n)
b=int(m)
for i in range(a+1,b):
  if (int(i))%2==0:
    k.append(str(i))
    print(i,end=" ")
