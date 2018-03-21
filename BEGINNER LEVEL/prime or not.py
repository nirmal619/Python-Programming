a=int(input())
for i in range(2,a+1):
  if(a%i==0):
    if(a==i):
      print("yes")
      break
    else:
      print("no")
      break
