def checkAlert(counts , days , checkDateValue):
	for i in range(1 , len(counts)):
		counts[i] += counts[i-1]

	for i in range(len(counts)):
		if(days % 2 != 0):
			if(counts[i] >= days // 2 + 1):
				if(checkDateValue >= 2 * i):
					return True
				return False
		else:
			if(counts[i] >= days // 2):
				for j in range(i , len(counts)):
					if(counts[j] >= days // 2 + 1):
						if(checkDateValue >= (i + j)):
							return True
						return False				


def findNumAlerts(transactions , days , n):
	num_alerts = 0
	counts = [0] * 201
	days_section = transactions[0:days]

	for spent in days_section:
		counts[spent] += 1

	for checkDate in range(days , n):

		if(checkAlert([num for num in counts] , days , transactions[checkDate])):
			num_alerts += 1

		counts[transactions[checkDate - days]] -= 1
		counts[transactions[checkDate]] += 1

	print(num_alerts)


n , days = list(map(int , input().split()))
transactions = list(map(int , input().split()))

findNumAlerts(transactions , days , n)