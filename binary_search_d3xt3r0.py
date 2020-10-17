def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	flag = False
	while( first<=last and not flag):
		temp = (first + last)//2
		if item_list[temp] == item :
			flag = True
		else:
			if item < item_list[temp]:
				last = temp - 1
			else:
				first = temp + 1	
	return flag
	
message = binary_search([4,5,6,8,9], 6)
print(message)