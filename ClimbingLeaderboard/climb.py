def binary_search(leaderboard , score , start , end):
	mid = (start + end) // 2

	if(start >= end):
		return mid
	elif(leaderboard[mid] > score):
		pos = binary_search(leaderboard , score , mid + 1 , end)
	else:
		pos = binary_search(leaderboard , score , 0 , mid)

	return pos

def findRanking(leaderboard , scores):
	rankings = []
	prev_score = 0

	for score in leaderboard:
		if(len(rankings) == 0):
			rankings.append(1)
			prev_score = score
			continue

		if(prev_score == score):
			rankings.append(rankings[-1])
		else:
			rankings.append(rankings[-1] + 1)

		prev_score = score

	return rankings


def determinePlayerProgress(leaderboard , rankings , scores , num_players , num_scores):
	for score in scores:
		placement = binary_search(leaderboard , score , 0 , num_players - 1)
		if(leaderboard[placement] > score):
			print(rankings[placement] + 1)
		else:
			print(rankings[placement])



num_players = int(input())
leaderboard = list(map(int , input().split()))

num_scores = int(input())
scores = list(map(int , input().split()))

determinePlayerProgress(leaderboard , findRanking(leaderboard , scores) , scores , num_players , num_scores)