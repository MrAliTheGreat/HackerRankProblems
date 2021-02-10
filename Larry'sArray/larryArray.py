def isSwapNeeded(numbers , low , high):
	middle = low + 1
	if(numbers[low] > numbers[middle] and numbers[middle] < numbers[high] and numbers[low] < numbers[high] or
	   numbers[low] > numbers[middle] and numbers[middle] < numbers[high] and numbers[low] > numbers[high]):
		return 1
	elif(numbers[low] < numbers[middle] and numbers[middle] > numbers[high] and numbers[low] > numbers[high] or
	     numbers[low] > numbers[middle] and numbers[middle] > numbers[high] and numbers[low] > numbers[high]):
		return 2
	else:
		return -1


def tripleSwap(numbers , low , high):
	middle = low + 1; temp = numbers[low];
	numbers[low] = numbers[middle]
	numbers[middle] = numbers[high]
	numbers[high] = temp


def isSortable(highest_value , numbers):
	hasSwapped = True
	while(hasSwapped):
		hasSwapped = False
		for low in range(highest_value - 2):
			isNeeded = isSwapNeeded(numbers , low , low + 2)
			if(isNeeded > 0):
				hasSwapped = True
				for _ in range(isNeeded):
					tripleSwap(numbers , low , low + 2)

	if(all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))):
		print("YES")
	else:
		print("NO")



num_tests = int(input())

for _ in range(num_tests):
	highest_value = int(input())
	numbers = list(map(int , input().split()))
	isSortable(highest_value , numbers)