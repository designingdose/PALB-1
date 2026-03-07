'''Given an integer array arr[] and an integer k, your task is to find and return the kth smallest
element in the given array.
Note: The kth smallest element is determined based on the sorted order of the array.
Examples:
Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
Output: 5
Explanation: 4th smallest element in the given array is 5.
Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output: 7
Explanation: 3rd smallest element in the given array is 7.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105
1 ≤ k ≤ arr.size()'''

def kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]


if __name__ == "__main__":
    # Take array input
    arr = list(map(int, input("Enter elements separated by space: ").split()))
    
    # Take k input
    k = int(input("Enter value of k: "))
    
    # Validation
    if k < 1 or k > len(arr):
        print("Invalid value of k")
    else:
        result = kth_smallest(arr, k)
        print(f"{k}th smallest element is:", result)