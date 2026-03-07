'''Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in
sorted order without using any extra space. Modify a[] so that it contains the first n elements and
modify b[] so that it contains the last m elements.
Examples:
Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
Output: a[] = [2, 2, 3, 4], b[] = [7, 10]
Explanation: After merging the two non-decreasing arrays, we get, [2, 2, 3, 4, 7, 10]
Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
Output: a[] = [1, 2, 3, 5, 8, 9], b[] = [10, 13, 15, 20]
Explanation: After merging two sorted arrays we get [1, 2, 3, 5, 8, 9, 10, 13, 15, 20].
Input: a[] = [0, 1], b[] = [2, 3]
Output: a[] = [0, 1], b[] = [2, 3]
Explanation: After merging two sorted arrays we get [0, 1, 2, 3].
Constraints:
1 ≤ n, m ≤ 105
0 ≤ a[i], b[i] ≤ 107'''

def mergeArrays(a, b):
    n = len(a)
    m = len(b)

    gap = (n + m + 1) // 2

    while gap > 0:
        i = 0
        j = gap

        while j < (n + m):

            # Case 1: both pointers in array a
            if i < n and j < n:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]

            # Case 2: i in a, j in b
            elif i < n and j >= n:
                if a[i] > b[j - n]:
                    a[i], b[j - n] = b[j - n], a[i]

            # Case 3: both in b
            else:
                if b[i - n] > b[j - n]:
                    b[i - n], b[j - n] = b[j - n], b[i - n]

            i += 1
            j += 1

        if gap == 1:
            gap = 0
        else:
            gap = (gap + 1) // 2

    return a, b


# -------- Input Section --------
a = list(map(int, input("Enter sorted array a: ").split()))
b = list(map(int, input("Enter sorted array b: ").split()))

# -------- Function Call --------
a, b = mergeArrays(a, b)

# -------- Output --------
print("Modified a:", a)
print("Modified b:", b)