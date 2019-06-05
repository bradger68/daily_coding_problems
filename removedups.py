#program that removes duplicates from a list.


myList = ["A", "B", "C", "A", "B", "C", "D", "D", "F"]
newList = []

def find_new_list(input):
	for i in myList:
		if i not in newList:
			newList.append(i)
		else:
			pass
	return newList
	
print(find_new_list(myList))
