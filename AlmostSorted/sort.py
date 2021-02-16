def isSwappable(quantity_numbers , numbers):
	back = -1; front = -1; num_falls = 0
	for i in range(quantity_numbers - 1):
		if(numbers[i] > numbers[i + 1]):
			if(back == -1):
				back = i
			else:
				front = i + 1
			num_falls += 1

	if(num_falls > 2):
		return False

	if(back == -1 and front == -1):
		print("yes")
		return True

	if(numbers[back] > numbers[front]):
		if(numbers[front - 1] < numbers[back] and (front + 1 >= quantity_numbers or numbers[back] < numbers[front + 1]) and
		   numbers[front] < numbers[back + 1] and (back - 1 < 0 or numbers[back - 1] < numbers[front])):
			
			print("yes")
			print("swap " + str(back + 1) + " " + str(front + 1))
			return True

	return False


def isReversable(quantity_numbers , numbers):
	head = -1; tail = -1; couples = []
	for i in range(quantity_numbers - 1):
		if(numbers[i] > numbers[i + 1] and head == -1):
			head = i
		if(numbers[i] < numbers[i + 1] and head != -1):
			tail = i
			couples.append((head , tail))
			head = -1; tail = -1

	if(len(couples) > 1):
		return False
	elif(len(couples) == 1):
		head = couples[0][0]; tail = couples[0][1]

	if(tail == -1):
		tail = quantity_numbers - 1

	if(tail + 1 >= quantity_numbers or numbers[head] < numbers[tail + 1] and
	   head - 1 < 0 or numbers[head - 1] < numbers[tail]):

		print("yes")
		if(tail - head == 1):
			print("swap " + str(head + 1) + " " + str(tail + 1))
		else:
			print("reverse " + str(head + 1) + " " + str(tail + 1))
		return True

	return False


def isSortable(quantity_numbers , numbers):
	if(not isSwappable(quantity_numbers , numbers)):
		if(not isReversable(quantity_numbers , numbers)):
			print("no")



quantity_numbers = int(input())
numbers = list(map(int , input().split()))

isSortable(quantity_numbers , numbers)
