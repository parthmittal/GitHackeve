def factorial(number_for_factorial):
	# Add code here
	return #Factorial number


def gcd(number_1, number_2):
	if number_1 < number_2:
		number_1, number_2 = number_2, number_1
	while number_2:
		number_1, number_2 = number_2, number_1 % number_2 #Cute implementation of Euler's GCD Algorithm
	return number_1

def is_palindrome(string_to_check):
	# Add code here
	return #boolean response


#Take input for fib in variable a

print(fib(a))


#Take input for is_prime in variable b, c

print(gcd(b, c))


#Take input for is_palindrome in variable d

print(is_palindrome(d))