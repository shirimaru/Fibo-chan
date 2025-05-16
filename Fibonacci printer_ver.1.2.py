while True:
 p = int(input("How many terms of the fibonacci series do you want to print?:"))

 def fibo(n):
   if(n==0 or n==1):
     return n
   else:
     return fibo(n-2) + fibo(n-1)
 n = 0
 while n < p:
  print(fibo(n))
  n = n + 1
