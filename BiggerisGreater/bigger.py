def countingSort(arrayNumbers):
	toBeSortedNumbers = [0] * 26
	sortedNumbers = [0] * len(arrayNumbers) 

	for num in arrayNumbers:
		toBeSortedNumbers[num] += 1

	for i in range(1 , len(toBeSortedNumbers)):
		toBeSortedNumbers[i] += toBeSortedNumbers[i-1]

	for num in arrayNumbers:
		toBeSortedNumbers[num] -= 1
		sortedNumbers[toBeSortedNumbers[num]] = num

	return sortedNumbers


def PivotTheList(wordNums):
	pivot = -1; successor = -1
	for i in range(len(wordNums) - 1 , 0 , -1):
		if(wordNums[i - 1] < wordNums[i]):
			pivot = i - 1
			break

	if(pivot == -1):
		return [] , []

	for i in range(pivot + 1 , len(wordNums)):
		if(wordNums[pivot] >= wordNums[i]):
			successor = i - 1
			break

		if(wordNums[pivot] < wordNums[i] and i == len(wordNums) - 1):
			successor = i

	temp = wordNums[pivot]
	wordNums[pivot] = wordNums[successor]
	wordNums[successor] = temp

	return wordNums[0 : pivot + 1] , countingSort(wordNums[pivot + 1 :])


def printNextWord(leftSide , rightSide):
	for num in leftSide:
		print(chr(num + 97) , end = "")

	for num in rightSide:
		print(chr(num + 97) , end = "")

	print()


def calculateNextWords(wordNums):
	leftSide , rightSide = PivotTheList(wordNums)
	if(leftSide == [] and rightSide == []):
		print("no answer")
	else:
		printNextWord(leftSide , rightSide)


def convertWordsToNumbers(word):
	numbers = []
	for letter in word:
		numbers.append(ord(letter) - 97)
	return numbers



num = int(input())

for _ in range(num):
	calculateNextWords(convertWordsToNumbers(input()))
