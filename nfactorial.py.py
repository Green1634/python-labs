def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
    
num = int(input("enter any value: "))


for n in range(num):  
    print(n, factorial_function(n))

