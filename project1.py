def fib(number_for_fibonacci):
	# Add code here
	return #Fibonacci number


def is_prime(number_to_check):
    a = True
    for i in range(int(number_to_check ** (0.5)) + 1):
        if number_to_check % i == 0:
            return False
    return True


def reverse_string(string_to_be_reversed):
	# Add code here
	return #reversed_string


#Take input for fib in variable a

print(fib(a))


#Take input for is_prime in variable b
b = int(input())
print(is_prime(b))


#Take input for reverse in variable c

print(reversed_string(c))
