Whenever George asks Lily to hang out, she's busy doing homework. George wants to help her finish it faster, but he's in over his head! Can you help George understand Lily's homework so she can hang out with him?

Consider an array of n distinct integers, arr = [a[0] , a[1] , ... , a[n-1]]. George can swap any two elements of the array any number of times. An array is beautiful if the sum of |arr[i] - arr[i-1]| among 0 < i < n is minimal.

Given the array arr, determine and return the minimum number of swaps that should be performed in order to make the array beautiful.

For example, arr = [7 , 15 , 12 , 3]. One minimal array is [3 , 7 , 12 , 15]. To get there, George performed the following swaps:

Swap      Result
      [7, 15, 12, 3]
3 7   [3, 15, 12, 7]
7 15  [3, 7, 12, 15]

It took 2 swaps to make the array beautiful. This is minimal among the choice of beautiful arrays possible.

Input Format

The first line contains a single integer, n, the number of elements in arr. The second line contains n space-separated integers arr[i].

Output Format

Return the minimum number of swaps needed to make the array beautiful.

Sample Input

4
2 5 3 1
Sample Output

2



***
Since this problem is a classic I have provided my solution's explaination here as well:
First of all if we have to understand what beautiful means here. Beautiful means that the list has to be sorted but remember that it can be sorted in increasing or decreasing order so we have to check both. Second thing to note, python is pointer based so you have to copy the lists that are being changed. After noting these points we traverse the list and compare it with the sorted list. If the elements are distinct we have to do a swap to at least make the place of one of them right it kinda revolves around greedy algorithm here but it makes sence cause you're at least putting one of them at the right place. Now where do we find the place of the sorted element in the primary list? preprocessing -> I used a dictionary to save the index of the elements and used it in the calculation but it's importent to note that when you swap the elements you have to change the dictionary values as well.
That's the total point of view. You can fully understand everything by taking a look at the code!
***
