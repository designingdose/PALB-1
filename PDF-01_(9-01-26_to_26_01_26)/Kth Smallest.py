'''Given an integer array arr[] and an integer k, your task is to find and return
the k
th smallest element in the given array.
Note: The kth smallest element is determined based on the sorted order of the
array.
Examples :
Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
Output: 5
Explanation: 4th smallest element in the given array is 5.'''

arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

arr.sort()
print("Kth Smallest Element:", arr[k-1])