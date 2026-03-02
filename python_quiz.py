#The code that prints the sum of the values from 1 to 3 using the print() function is print(1+2+3). With reference to this code, print the sum of the values from 1 to 5 as follows
print(1+2+3+4+5)

#The figure below is a flowchart of a program that finds the sum of odd numbers among integers between 1 and 100 and prints the sum. Fill in the blanks in the second figure of the following flowchart
N = 1
S = 0
while N <= 100:
    S = S + N
    N = N + 2
print(S)

#We will write a program that receives a positive integer from the user and tells whether it is an odd or even number. Complete the appropriate pseudo code for the underlined part
print("Enter an integer:")
n = int(input())
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")
    
#Write a code to print the following decorative output. In the first line, use only one '*' character with the operator * and 
'''number. In the second line, use only one '#' character and one space with the operator * and number.
Coding guideline: In the case of the first line, print in the same way as '*' * number n. The second line also uses the * 
operator '''
n = 40
print('*' * n)
print('# ' * n)   

#Write and save the following name and address in the name and address variables, respectively. Write a code that prints them to the screen
name = "David Doe"
address = "1600 Wilshire Blvd #205, Los Angeles CA 90017"
print(name)
print(address)

#Expect the output of the following code and write it down
x = 1
y = 0
print(x and y)
print(x or y)
print(not x)
print(not y)

#Write a program that takes two random integers as input and lists them from smallest to largest.
'''(Condition: Two integers are not the same number.)
Coding guideline: Receive the user's input with the input function and convert it to an integer using the intfunction. 
Next, use an if statement to compare and print the two values'''
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
if num1 < num2:
    print(num1, num2)
else:
    print(num2, num1)
    
#Write a program that performs the following using a compound conditional expression of an if statement.
'''Coding guideline: Write a code that performs differently depending on whether the answer to the first question is 0 or 1, 
as shown below'''
adult = int(input("Are you an adult? (1 if you are an adult, 0 if you are minor): "))
married = int(input("Are you married? (1 if you are married, 0 if you are single): "))
if adult == 1 and married == 1:
    print("You are an adult who is married.")
elif adult == 1 and married == 0:
    print("You are an adult who is single.")
elif adult == 0 and married == 1:
    print("You are a minor who is married.")
else:
    print("You are a minor who is single.")    
    
    
#Among the positive natural numbers other than 1, a number that is not prime is called a composite number. Print the 
'''prime and composite numbers from 2 to 12 as follows.
Coding guideline: Use the for statement to solve this problem. When using a nested for statement, an expression for 
determining a prime number must be entered in the inner for statement'''
for num in range(2, 13):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, ": Prime number")
    else:
        print(num, ": Composite number")
        
#An Armstrong number is a three-digit integer that is equal to the sum of the cubes of each digit. Find all Armstrong 
'''numbers among three-digit integers and print them as follows.
Coding guideline: All numbers from 100 to 999 should be searched using the for statement '''
for num in range(100, 1000):
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    if num == hundreds**3 + tens**3 + ones**3:
        print(num)       
        
#If there are two lists l1 and l2 with the following strings, use the combination of l1 and l2 to print as follows.Coding guideline: Use nested loops to print it out  
l1 = ['I like', 'I love']
l2 = ['pancake.', 'kiwi juice.', 'espresso.']
for phrase1 in l1:
    for phrase2 in l2:
        print(phrase1, phrase2)      
        
#The person dictionary is defined as follows. Add a new item to this person dictionary with the key 'Father' and the value 
''''John Doe'. And then print the person dictionary.
Coding guideline: After defining the person dictionary, write a code to add new items  '''
person = {'Name': 'David Doe', 'Age': 26, 'Weight': 82, 'Job': 'Data scientist'}
person['Father'] = 'John Doe'
print(person)      

#With tuple data, the values of two variables can be swapped without using a temporary variable. Using this swapping 
'''method, write a program that moves the largest value in the given list to the last.
Coding guideline: Use a for loop. When swapping values in a list, additional variables such as temp should not be used'''
lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]
max_index = 0
for i in range(len(lst)):
    if lst[i] > lst[max_index]:
        max_index = i
lst[max_index], lst[-1] = lst[-1], lst[max_index]
print(lst)

#The two-dimensional array a contains the values [[1, 2], [3, 4], [5, 6]]. Change this two-dimensional array to a one
'''dimensional array like [1, 2, 3, 4, 5, 6], and print it out.
Coding guideline: Use a for loop. Define a new array and put the elements of a into this array'''
a = [[1, 2], [3, 4], [5, 6]]
new_list = []
for sublist in a:
    for element in sublist:
        new_list.append(element)
print(new_list)

#There is a dictionary variable mariaas follows. In this dictionary variable, courses such as ‘korean' and ‘english' and their 
'''scores are stored as key:value. Print the average score of 89.25 for maria'ssubject scores.
Coding guideline: Use a dictionary method such as values() and len() function'''
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average = sum(maria.values()) / len(maria)
print(average)

#Declare a nested dictionary school as follows. Next, use the deepcopy() function of the copy module to write a program 
'''that 'copy' to another variable, school2. (Check that school and school2are different variables through the is operator.) 
Coding guideline: Print so that the result of school is school2is false'''
import copy
school = {
    'kim': {'age': 16, 'hei': 170, 'grade': 3},
    'lee': {'age': 15, 'hei': 168, 'grade': 2},
    'choi': {'age': 14, 'hei': 173, 'grade': 1}
}
school2 = copy.deepcopy(school)
print(school is school2)

#There is a scores tuple as follows. This tuple contains information about four students, including each student's name 
'''and English, math, and science grades. For example, ‘Hyun’ has an English score of 88, a math score of 95, and a science 
score of 90. Extract only math scores by unpacking the scores tuple. Write a code that calculates the average of these 
extracted math scores.
Coding guideline: Use the zip function to solve the problem'''
scores = (('Hyun', 88, 95, 90),
          ('Kang', 85, 90, 95),
          ('Park', 70, 90, 80),
          ('Hong', 90, 90, 95))
names, english, math, science = zip(*scores)
average_math = sum(math) / len(math)
print(average_math)