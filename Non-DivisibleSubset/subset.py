def getOptimalSubset(numbers , num_numbers , k):
	dict_remainders = {}
	visited = [False] * k
	max_subset_size = 0

	for num in numbers:
		if((num % k) not in dict_remainders.keys()):
			dict_remainders[num % k] = [num]
		else:
			dict_remainders[num % k].append(num)

	for dict_key in dict_remainders.keys():
		if(dict_key == 0):
			max_subset_size += 1
			continue

		if(visited[dict_key] == False):
			if((k - dict_key) in dict_remainders.keys()):
				if(k - dict_key != dict_key):
					max_subset_size += max(len(dict_remainders[dict_key]) , len(dict_remainders[k - dict_key]))
					visited[dict_key] = True ; visited[k - dict_key] = True
				else:
					max_subset_size += 1
					continue
			else:
				max_subset_size += len(dict_remainders[dict_key])
				visited[dict_key] = True

	print(max_subset_size)



num_numbers , k = list(map(int , input().split()))

numbers = [int(x) for x in input().split()]

getOptimalSubset(numbers , num_numbers , k)