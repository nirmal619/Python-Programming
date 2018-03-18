try:
  a=int(input())
  b=int(input())
  c=int(input())
except:
  print("invalid code")
else:
  if(a>b and a>c):
    print("a is greater")
  elif(b>a and b>c):
    print("b is greater")
  elif(c>b and c>a):
    print("c is greater")
