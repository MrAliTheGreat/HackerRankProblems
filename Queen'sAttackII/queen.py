def getOriginalNumDangered(n , queen_row , queen_column):
	return 2 * n - 2 + (min(n - queen_row , queen_column - 1) + 
						min(n - queen_row , n - queen_column) + 
						min(queen_row - 1 , queen_column - 1) + 
						min(queen_row - 1 , n - queen_column))


def findNumDangered(n , queen_row , queen_column , obstacles):
	prev_decreased = [0] * 8  # left , right , up , down , leftUp , rightUp , leftDown , rightDown
	NumDangered = getOriginalNumDangered(n , queen_row , queen_column)

	for obstacle_row , obstacle_column in obstacles:

		if(obstacle_row == queen_row):
			if(obstacle_column < queen_column):
				if(obstacle_column > prev_decreased[0]):
					NumDangered -= (obstacle_column - prev_decreased[0])
					prev_decreased[0] = obstacle_column
			
			else:
				if((n - obstacle_column + 1) > prev_decreased[1]):
					NumDangered -= (n - obstacle_column + 1 - prev_decreased[1])
					prev_decreased[1] = (n - obstacle_column + 1)

		
		if(obstacle_column == queen_column):
			if(obstacle_row < queen_row):
				if(obstacle_row > prev_decreased[3]):
					NumDangered -= (obstacle_row - prev_decreased[3])
					prev_decreased[3] = obstacle_row
			
			else:
				if((n - obstacle_row + 1) > prev_decreased[2]):
					NumDangered -= (n - obstacle_row + 1 - prev_decreased[2])
					prev_decreased[2] = (n - obstacle_row + 1)

		
		if(abs(obstacle_row - queen_row) == abs(obstacle_column - queen_column)):
			if(queen_row - obstacle_row < 0 and queen_column - obstacle_column > 0): # left up
				if((min(n - obstacle_row , obstacle_column - 1) + 1) > prev_decreased[4]):
					NumDangered -= (min(n - obstacle_row , obstacle_column - 1) + 1 - prev_decreased[4])
					prev_decreased[4] = min(n - obstacle_row , obstacle_column - 1) + 1
			
			
			elif(queen_row - obstacle_row < 0 and queen_column - obstacle_column < 0): # right up
				if((min(n - obstacle_row , n - obstacle_column) + 1) > prev_decreased[5]):
					NumDangered -= (min(n - obstacle_row , n - obstacle_column) + 1 - prev_decreased[5])
					prev_decreased[5] = (min(n - obstacle_row , n - obstacle_column) + 1)
	
			
			elif(queen_row - obstacle_row > 0 and queen_column - obstacle_column > 0): # left down
				if((min(obstacle_row - 1 , obstacle_column - 1) + 1) > prev_decreased[6]):
					NumDangered -= (min(obstacle_row - 1 , obstacle_column - 1) + 1 - prev_decreased[6])
					prev_decreased[6] = (min(obstacle_row - 1 , obstacle_column - 1) + 1)

			
			else: # right down
				if((min(obstacle_row - 1 , n - obstacle_column) + 1) > prev_decreased[7]):
					NumDangered -= (min(obstacle_row - 1 , n - obstacle_column) + 1 - prev_decreased[7])
					prev_decreased[7] = (min(obstacle_row - 1 , n - obstacle_column) + 1)

	print(NumDangered)



obstacles = []

n , k = tuple(map(int , input().split()))

queen_row , queen_column = tuple(map(int , input().split()))

for _ in range(k):
	obstacles.append(tuple(map(int , input().split())))

findNumDangered(n , queen_row , queen_column , obstacles)