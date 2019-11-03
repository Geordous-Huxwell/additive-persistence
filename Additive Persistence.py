def addDigits(num):
	total = 0
	while(num):
		total += num%10
		num //= 10
	return total

def calcAdditivePersistence(num):	#using while loop
	additivePersistence = 0
	while(num>9):
		num = addDigits(num)
		additivePersistence += 1
	return additivePersistence

def calcAdditivePersistenceRec(num):	#using recursion
	if(num <= 9):
		return 0
	else:
		return 1+calcAdditivePersistenceRec(addDigits(num))

a = 9991
print(calcAdditivePersistence(a))
print(calcAdditivePersistenceRec(a))