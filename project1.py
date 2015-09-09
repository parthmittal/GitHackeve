def fib(number_for_fibonacci):
	# Add code here
	a, b = 0, 1
	for i in range (1, number_for_fibonacci)
		a, b = b, a + b
	return b


def is_prime(number_to_check):
    a = True
    for i in range(int(number_to_check ** (0.5)) + 1):
        if number_to_check % i == 0:
            return False
    return True


def reverse_string(string_to_be_reversed):
	return string_to_be_reversed[::-1]


#Take input for fib in variable a
a = int(input("Number for fibonacci: "))
print(fib(a))


#Take input for is_prime in variable b
b = int(input())
print(is_prime(b))


c = input ()

print(reversed_string(c))
