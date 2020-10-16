#python code which returns true if the given string is a palindrome else false.

def isPalindrome(imput_string):
	reverse_string = imput_string[::-1]
	reverse_string = reverse_string.lowercase()
	imput_string  = imput_string.lowercase()
	return imput_string == reverse_string


checkstring = str(input("Enter the input string: "))

if isPalindrome(checkstring):
	print("Yes, it is a palindrome,")
else:
	print("No, it is not a palindrome.")
