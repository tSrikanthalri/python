#WAPT chech how many elements to count how many elements present in a given string
'''
given_string = input('Enter the string: ') #taking input from user.

count = 0                                  #taking empty count variable for count purpose.
for element in given_string:              #Using for loop for iteration of elements in given_string.
    count += 1                            #incresing count variable by 1 if element is present in given_string.
print(f'count of the given string: {count}') #printing the count variable. '''


#WAPT how many times a givensubstiring is present in given_string
'''
s1 = input('Enter the string: ')      #taking input1 from user(string input)
s2 = input('Enter the substring: ')   #taking input2 from user (substring input)

count = 0                             #initially taking empty count variable for count purpose.                         
for element in s1:                    #Using for loop for iteration of elements in s1.
    if element == s2:                 #Using if condition for checking condition.
        count += 1                    #incresing count variable by 1 
print(f'count of the s1 : {count}')    #printing the count variable.'''


#WAPT count the vowels in given string
'''
given_string = input('Enter the string: ')  #taking input from user.

count = 0                                   #taking empty count variable for count purpose.                                       
for element in given_string:                #Using for loop for iteration of elements in given_string.
    if element in ('A','E','I','O','U','a','e','i','o','u'):  #Using if condition for checking condition.
        count +=1                           #incresing count variable by 1.
print(f'count of the s1 : {count}')   #printing the count variable.'''

#WAPT CONSONANTS present in given string
'''
s1 = input('enter the string')       #taking input1 from user(string input)

count=0                               #taking empty count variable for count purpose.     
for element in s1:                  #Using for loop for iteration of elements in s1
    if element.isalpha():           #Using if condition for checking condition
        if element not in ('A','E','I','O','U','a','e','i','o','u'):  
            count += 1            #incresing count variable by 1.
print(f'count of the s1 : {count}')    #printing the count variable.  '''

#WAPT special character are present in given string

given_string = input('Enter the string: ')  #taking input from user.

count = 0 #taking empty count variable for count purpose.
for element in given_string: #Using for loop for iteration of elements in given_string.
    if element.isalnum() == False:  #Using if condition for checking condition
        count += 1                 ##incresing count variable by 1.
print(f'count of the s1 : {count}')    #printing the count variable.
    

 

