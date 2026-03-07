'''Given three sorted arrays in non-decreasing order, print all common elements 
in non-decreasing order across these arrays. If there are no such elements return 
an empty array. In this case, the output will be -1.
Note: can you handle the duplicates without using any additional Data Structure?
Examples :
Input: arr1 = [1, 5, 10, 20, 40, 80] , arr2 = [6, 7, 20, 80, 100] , arr3 = [3, 4, 15, 20, 
30, 70, 80, 120]
Output: [20, 80]
Explanation: 20 and 80 are the only common elements in arr1, arr2 and arr3.
Input: arr1 = [1, 2, 3, 4, 5] , arr2 = [6, 7] , arr3 = [8,9,10]
Output: [-1]
Explanation: There are no common elements in arr1, arr2 and arr3.
Input: arr1 = [1, 1, 1, 2, 2, 2], arr2 = [1, 1, 2, 2, 2], arr3 = [1, 1, 1, 1, 2, 2, 2, 2]
Output: [1, 2]
Explanation: We do not need to consider duplicates Given an integer n, find its factorial. Return a list of integers denoting the digits 
that make up the factorial of n.
Examples:
Input: n = 5
Output: [1, 2, 0]
Explanation: 5! = 1*2*3*4*5 = 120
Input: n = 10
Output: [3, 6, 2, 8, 8, 0, 0]
Explanation: 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800
Input: n = 1
Output: [1]
Explanation: 1! = 1'''
def factorial(n):
    result = [1]
    
    for i in range(2, n + 1):
        carry = 0
        
        for j in range(len(result)):
            prod = result[j] * i + carry
            result[j] = prod % 10
            carry = prod // 10
        
        while carry:
            result.append(carry % 10)
            carry //= 10
    
    result.reverse()
    return result

n = int(input("Enter n: "))

print("Factorial digits:", factorial(n))