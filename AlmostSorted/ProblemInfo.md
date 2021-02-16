Given an array of integers, determine whether the array can be sorted in ascending order using only one of the following operations one time.
1. Swap two elements.
2. Reverse one sub-segment.

Determine whether one, both or neither of the operations will complete the task. Output is as follows.
1. If the array is already sorted, output yes on the first line. You do not need to output anything else.

2. If you can sort this array using one single operation (from the two permitted operations) then output yes on the first line and then:

If elements can only be swapped, d[l] and d[r], output swap l r in the second line. l and r are the indices of the elements to be swapped, assuming that the array is indexed from 1 to n.
If elements can only be reversed, for the segment d[l..r], output reverse l r in the second line. l and r are the indices of the first and last elements of the subarray to be reversed, assuming that the array is indexed from 1 to n. Here d[l..r] represents the subarray that begins at index l and ends at index r, both inclusive.
If an array can be sorted both ways, by using either swap or reverse, choose swap.

3. If the array cannot be sorted either way, output no on the first line.

Example:
arr = [2,3,5,4]

Either swap the 4 and 5, or reverse them to sort the array. As mentioned above, swap is preferred over reverse. Choose swap. On the first line, print yes. On the second line, print swap 3 4.


Sample Input 1

2
4 2
Sample Output 1

yes
swap 1 2
Explanation 1

You can either swap(1, 2) or reverse(1, 2). You prefer swap.

Sample Input 2

3
3 1 2
Sample Output 2

no
Explanation 2

It is impossible to sort by one single operation.

Sample Input 3

6
1 5 4 3 2 6
Sample Output 3

yes
reverse 2 5
Explanation 3

You can reverse the sub-array d[2...5] = "5 4 3 2", then the array becomes sorted.
