'''Given an array arr[] denoting heights of n towers and a positive integer k.
For each tower, you must perform exactly one of the following operations exactly once.
Increase the height of the tower by k
Decrease the height of the tower by k
Find out the minimum possible difference between the height of the shortest and tallest towers
after you have modified each tower.
You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by k for each tower. After the operation,
the resultant array should not contain any negative integers.
Examples :
Input: k = 2, arr[] = [1, 5, 8, 10]
Output: 5
Explanation: The array can be modified as [1+k, 5-k, 8-k, 10-k] = [3, 3, 6, 8]. The difference
between the largest and the smallest is 8-3 = 5.
Input: k = 3, arr[] = [3, 9, 12, 16, 20]
Output: 11
Explanation: The array can be modified as [3+k, 9+k, 12-k, 16-k, 20-k] = [6, 12, 9, 13, 17]. The
difference between the largest and the smallest is 17-6 = 11.
Constraints
1 ≤ k ≤ 107
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 107'''

def minimize_heights(arr, k):
    n = len(arr)
    
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Initial difference
    ans = arr[n - 1] - arr[0]
    
    # Step 3: Smallest and largest after modification
    for i in range(1, n):
        
        # If decreasing makes negative, skip
        if arr[i] - k < 0:
            continue
        
        minimum = min(arr[0] + k, arr[i] - k)
        maximum = max(arr[i - 1] + k, arr[n - 1] - k)
        
        ans = min(ans, maximum - minimum)
    
    return ans


if __name__ == "__main__":
    k = int(input("Enter value of k: "))
    arr = list(map(int, input("Enter tower heights: ").split()))
    
    print("Minimum difference:", minimize_heights(arr, k))