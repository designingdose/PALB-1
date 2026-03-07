'''You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the 
array is sorted in non-decreasing order. Your task is to find and return the index of the 
first row that contains the maximum number of 1s. If no such row exists, return -1.
Note:
• The array follows 0-based indexing.
• The number of rows and columns in the array are denoted 
by n and m respectively.
Examples:
Input: arr[][] = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
Output: 2
Explanation: Row 2 contains the most number of 1s (4 1s). Hence, the output is 2.
Input: arr[][] = [[0,0], [1,1]]
Output: 1
Explanation: Row 1 contains the most number of 1s (2 1s). Hence, the output is 1.
Input: arr[][] = [[0,0], [0,0]]
Output: -1
Explanation: No row contains any 1s, so the output is -1.'''

def rowWithMax1s(arr):
    n = len(arr)
    m = len(arr[0])

    max_count = 0
    index = -1

    for i in range(n):
        count = arr[i].count(1)

        if count > max_count:
            max_count = count
            index = i

    return index


# Input
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix = []
print("Enter matrix rows:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Row with maximum 1s index:", rowWithMax1s(matrix))