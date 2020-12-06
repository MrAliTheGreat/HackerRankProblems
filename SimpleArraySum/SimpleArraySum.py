def sumNumbers(nums):
	sum = 0
	for num in nums:
		sum += num

	return sum



size = int(input())
nums = list(map(int , input().split()))

print(sumNumbers(nums))