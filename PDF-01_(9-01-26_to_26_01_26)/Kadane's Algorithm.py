'''You are given an integer array arr[]. You need to find the maximum sum of a 
subarray (containing at least one element) in the array arr[].
Note : A subarray is a continuous part of an array.
Examples:
Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.'''

def max_subarray_sum(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


arr = list(map(int, input("Enter elements separated by space: ").split()))

result = max_subarray_sum(arr)

print("Maximum Subarray Sum:", result)
