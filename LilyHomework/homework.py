def swapNumbers(numbers , index_numbers , idx_1 , idx_2):
	index_numbers[numbers[idx_1]] = idx_2; index_numbers[numbers[idx_2]] = idx_1 
	temp = numbers[idx_1]
	numbers[idx_1] = numbers[idx_2]
	numbers[idx_2] = temp


def calculateNumberOfSwaps(numbers , sorted_numbers , index_numbers , quantity_numbers):
	num_swaps = 0
	for i in range(quantity_numbers):
		if(numbers[i] != sorted_numbers[i]):
			swapNumbers(numbers , index_numbers , i , index_numbers[sorted_numbers[i]])
			num_swaps += 1

	return num_swaps


def findNumSwaps(numbers , quantity_numbers):
	index_numbers = {}
	sorted_numbers = sorted(numbers)

	for i in range(quantity_numbers):
		index_numbers[numbers[i]] = i

	print(min(calculateNumberOfSwaps([num for num in numbers] , sorted_numbers , dict(index_numbers) , quantity_numbers) ,
		      calculateNumberOfSwaps(numbers , sorted_numbers[::-1] , index_numbers , quantity_numbers)))



quantity_numbers = int(input())
numbers = list(map(int , input().split()))

findNumSwaps(numbers , quantity_numbers)