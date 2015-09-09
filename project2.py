def factorial(number_for_factorial):
	# Add code here
	factorial = 1
	while(number_for_factorial):
		factorial *= number_for_factorial
		number_for_factorial -= 1
	return factorial#Factorial number


def gcd(number_1, number_2):
	if number_1 < number_2:
		number_1, number_2 = number_2, number_1
	while number_2:
		number_1, number_2 = number_2, number_1 % number_2 #Cute implementation of Euler's GCD Algorithm
	return number_1

def is_palindrome(string_to_check):
    return string_to_check == string_to_check[::-1] 


#Take input for fib in variable a
a = int(input())
print(factorial(a))


#Take input for is_prime in variable b, c

print(gcd(b, c))


#Take input for is_palindrome in variable d
d = input('Enter string to check for palindrome: ')
print(is_palindrome(d))
