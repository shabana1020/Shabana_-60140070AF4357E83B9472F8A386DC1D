def fact_rec(n) :
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)
num=int(input("Enter a value"))
rec=fact_rec(num)
print("the factorial of {} is {}.".format(num, rec))