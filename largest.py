# Python program for the above approach

# Function to find the largest palindrome
# not exceeding N which can be expressed
# as the product of two 3-digit numbers
def palindrome_prod(N):

	# Stores all palindromes
	palindrome_list = []
	
	for i in range(101, 1000):
		for j in range(121, 1000, (1 if i % 11 == 0 else 11)):
			
			# Stores the product
			n = i * j
			x = str(n)
			
			# Check if X is palindrome
			if x == x[::-1]:
			
				# Check n is less than N
				if n < N:
				
					# If true, append it
					# in the list
					palindrome_list.append(i * j)

	# Print the largest palindrome
	print(max(palindrome_list))

# Driver Code

N = 101110

# Function Call
palindrome_prod(N)
