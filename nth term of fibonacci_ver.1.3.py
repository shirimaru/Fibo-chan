def fibo(n):
  if(n==0 or n==1):
    return n
  else:
    return fibo(n-1)+fibo(n-2)
while True:
  try:
    n = int(input("Enter your number:"))
    print(f"The {n}th term is {fibo(n)}")
    break
  except Exception as e:
    print("Please enter integer values only.")

    
