HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to 2 times the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days d and a client's total daily expenditures for a period of n days, find and print the number of times the client will receive a notification over all n days.

For example, d = 3 and expenditures = [10 , 20 , 30 , 40 , 50]. On the first three days, they just collect spending data. At day 4, we have trailing expenditures of [10 , 20 , 30]. The median is 20 and the day's expenditure is 40. Because 40 is more than or equal to 2 * 20, there will be a notice. The next day, our trailing expenditures are [20 , 30 , 40] and the expenditures are 50. This is less than 2 * 30 so no notice will be sent. Over the period, there was one notice sent.


Input Format

The first line contains two space-separated integers n and d, the number of days of transaction data, and the number of trailing days' data used to calculate median spending.
The second line contains n space-separated non-negative integers where each integer  denotes expenditure[i].


Sample Input 0

9 5
2 3 4 2 3 6 8 4 5
Sample Output 0

2


Sample Input 1

5 4
1 2 3 4 4
Sample Output 1

0

Importent Note!!!
0 <= expenditure[i] <= 200



*** HINTS ***

4 thoughts that may help:

1.) Counting sort

2.) A Queue

3.) Pay attention to the even case.

4.) Integer division is a blessing and a curse, be careful.


