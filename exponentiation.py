'''Efficient approach'''

def bin_pow(a,n):
	res = 1
	while(n>0):
		if n&1:
			res = res * a
		a = a * a
		n >>= 1
	return res
print(bin_pow(2101010,32)) #20782597351780148360705447543438026166282198412508937706220746225693908693563681788663888827908012942663696008670876015403914749631306435949260373147394419808970340368320100000000000000000000000000000000

'''  Time complexity : O(log n) '''