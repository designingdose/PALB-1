'''Given an array arr[]. Your task is to find the minimum and maximum elements
in the array.
Examples:
Input: arr[] = [1, 4, 3, 5, 8, 6]
Output: [1, 8]
Explanation: minimum and maximum elements of array are 1 and 8.
'''

def get_min_max(arr):
    minimum = arr[0]
    maximum = arr[0]

    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum


arr = list(map(int, input("Enter elements separated by space: ").split()))

minimum, maximum = get_min_max(arr)

print("Minimum:", minimum)
print("Maximum:", maximum)