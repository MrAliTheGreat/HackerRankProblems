Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S' is not evenly divisible by k.

For example, the array S = [19 , 10 , 12 , 10 , 24 , 25 , 22] and k = 4. One of the arrays that can be created is S'[0] = [10 , 12 , 25]. Another is S'[1] = [19 , 22 , 24]. After testing all permutations, the maximum length solution array has 3 elements.

The first line contains 2 space-separated integers, n and k , the number of values in S and the non factor.
The second line contains n space-separated integers describing S[i], the unique values of the set.


Sample Input

4 3
1 7 2 4

Sample Output

3
