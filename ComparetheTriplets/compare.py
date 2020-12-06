def compare(firstPersonNums , SecondPersonNums):
	scoreFirstPerson = 0;
	scoreSecondPerson = 0;
	for i in range(3):
		if(firstPersonNums[i] > SecondPersonNums[i]):
			scoreFirstPerson += 1
		elif(firstPersonNums[i] < SecondPersonNums[i]):
			scoreSecondPerson += 1

	print(str(scoreFirstPerson) + " " + str(scoreSecondPerson))


firstPersonNums = list(map(int , input().split()))
SecondPersonNums = list(map(int , input().split()))

compare(firstPersonNums , SecondPersonNums)