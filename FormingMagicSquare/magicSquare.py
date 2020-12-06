def findOptimalCost(square , possibleSquares):
	optimalCost = float("inf")
	cost = 0

	for possibleSquare in range(len(possibleSquares)):
		for i in range(len(square)):
			for j in range(len(square[i])):
				cost += abs(possibleSquares[possibleSquare][i][j] - square[i][j])

		if(cost < optimalCost):
			optimalCost = cost

		cost = 0

	print(optimalCost)


square = []

possibleSquares = [[[8 , 1 , 6] , [3 , 5 , 7] , [4 , 9 , 2]] , 
				   [[6 , 1 , 8] , [7 , 5 , 3] , [2 , 9 , 4]] ,
				   [[4 , 9 , 2] , [3 , 5 , 7] , [8 , 1 , 6]] ,
				   [[2 , 9 , 4] , [7 , 5 , 3] , [6 , 1 , 8]] ,
				   [[8 , 3 , 4] , [1 , 5 , 9] , [6 , 7 , 2]] ,
				   [[4 , 3 , 8] , [9 , 5 , 1] , [2 , 7 , 6]] ,
				   [[6 , 7 , 2] , [1 , 5 , 9] , [8 , 3 , 4]] ,
				   [[2 , 7 , 6] , [9 , 5 , 1] , [4 , 3 , 8]]]

for _ in range(3):
	square.append(list(map(int , input().split())))

findOptimalCost(square , possibleSquares)
