def generate_absPerm(num_range , diff):
	absPerm = [0] * num_range
	visited = [False] * num_range

	last_index = num_range - 1
	
	for i in range(diff):
		if(i + diff > last_index):
			print(-1)
			return
		
		absPerm[i] = i + diff + 1; visited[i + diff] = True
		
		if(visited[last_index - i - diff] or last_index - i - diff < 0):
			print(-1)
			return
		
		absPerm[last_index - i] = last_index - i - diff + 1; visited[last_index - i - diff] = True

	for pos in range(diff , num_range - diff):
		if(visited[pos - diff] and visited[pos + diff]):
			print(-1)
			return
		elif(visited[pos - diff]):
			absPerm[pos] = pos + diff + 1; visited[pos + diff] = True
		else:
			absPerm[pos] = pos - diff + 1; visited[pos - diff] = True

	print(" ".join(map(str , absPerm)))



num_tests = int(input())

for _ in range(num_tests):
	num_range , diff = list(map(int , input().split()))
	generate_absPerm(num_range , diff)
	
