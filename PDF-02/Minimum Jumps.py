'''You are given an array arr[] of non-negative numbers. Each number tells you the maximum
number of steps you can jump forward from that position.
For example:
If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
If arr[i] = 0, you cannot jump forward from that position.
Your task is to find the minimum number of jumps needed to move from the first position in the
array to the last position.
Note: Return -1 if you can't reach the end of the array.
Examples :
Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
Output: 3
Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th
element with value 9, and from here we will jump to the last.
Input: arr = [1, 4, 3, 2, 6, 7]
Output: 2
Explanation: First we jump from the 1st to 2nd element and then jump to the last element.
Input: arr = [0, 10, 20]
Output: -1
Explanation: We cannot go anywhere from the 1st element.
Constraints:
2 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105
'''

def min_jumps(arr):
    n = len(arr)
    
    # If array has only one element
    if n == 1:
        return 0
    
    # If first element is 0, cannot move
    if arr[0] == 0:
        return -1
    
    jumps = 1
    current_end = arr[0]
    farthest = arr[0]
    
    for i in range(1, n):
        
        # If we reached last index
        if i == n - 1:
            return jumps
        
        farthest = max(farthest, i + arr[i])
        
        # If we reached end of current jump range
        if i == current_end:
            jumps += 1
            
            if farthest <= i:
                return -1
            
            current_end = farthest
    
    return -1


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    print("Minimum jumps:", min_jumps(arr))