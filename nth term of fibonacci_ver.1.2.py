while True:
 def fibo(n):
   if(n==0 or n==1):
     return n
   else:
     return fibo(n-2) + fibo(n-1)
 n = int(input("Enter the value of n:"))
 print(f"The value {n}th term of fibonacci series is {fibo(n)}")

 
