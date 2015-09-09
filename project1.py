def fib(number_for_fibonacci):
	# Add code here
	a = [0,1]
	i = 2
	while(len(a)<number_for_fibonacci):
		a.append(a[i-1] + a[i-2])
	return a[number_for_fibonacci] #Fibonacci number


def is_prime(number_to_check):
    # Add code here
    return #boolean value


def reverse_string(string_to_be_reversed):
	# Add code here
	return #reversed_string


#Take input for fib in variable a
a = int(input("Number for fibonacci: "))
print(fib(a))


#Take input for is_prime in variable b

print(is_prime(b))


#Take input for reverse in variable c

print(reversed_string(c))