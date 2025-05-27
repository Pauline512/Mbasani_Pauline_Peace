fac = lambda x: x * fac(x-1) if x >= 2 else 1
num = int(input("Enter a number to find the factorial: "))
print("Factorial: {}".format(fac(num)))
