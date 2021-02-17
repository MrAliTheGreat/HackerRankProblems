def calculateSurface(cubes , num_rows , num_columns):
	surface = 0;
	for i in range(num_rows):
		for j in range(num_columns):
			surface += (2 + cubes[i][j] * 4)
			if(i - 1 >= 0): # upper row
				surface -= min(cubes[i - 1][j] , cubes[i][j])
			if(i + 1 < num_rows): # lower row
				surface -= min(cubes[i + 1][j] , cubes[i][j])
			if(j - 1 >= 0): # left column
				surface -= min(cubes[i][j - 1] , cubes[i][j])
			if(j + 1 < num_columns): # right column
				surface -= min(cubes[i][j + 1] , cubes[i][j])

	print(surface)



cubes = []
num_rows , num_columns = list(map(int , input().split()))

for _ in range(num_rows):
	cubes.append(list(map(int , input().split())))

calculateSurface(cubes , num_rows , num_columns)