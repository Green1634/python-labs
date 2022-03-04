def is_prime(num):
    if num == 2 or num ==3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        return True
#
# Write your code here.
#


for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print(is_prime)
