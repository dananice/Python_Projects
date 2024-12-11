'''
Instructions
Good evening folks, as requested, here are some fun brainteasers, please give them a try and feel free to hand back for some extra points. Don't forget to have fun solving these!
'''
'''
You have 2 lists, extract and remove the data from one list and place the items in the other. Print your result
'''
# had to research this as my way stopped looping at 5.  Don't understand why the long way didn't work

first_list = [1,2,3,4,5,6,7,8,9,10]

second_list = []

# # length of first_list
for i in range(len(first_list)):
# # # loop to place item in second_list using append while removing from first list
    second_list.append(first_list.pop(0))
    print(f'This is the second_list: ',second_list)
    print(f'This is the first list after removal of zero index: ' ,first_list)


'''
 Write a  Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.
Input: 123456789
Output:
945
Input: 2468
Output:
0
Input: 13579
Output:
945

'''
''' This took a minute to complete my syntax was off.  I used the vowels example and a little research to complete.  I knew what I needed to complete just wasn't sure where everything went '''
number = (input('Please enter a number: '))


# # Find the odd digits
if any(int(n) % 2 for n in str(number)):
#     # store odd numbers
    product = 1
#     # loop over every digit in number
    for n in str(number):
#         # calculate the product of the odd digits
        if int(n) % 2 == 1:
            product *= int(n) 
  
# # print the results 
    print(product)
print(f'0: There are no odd digits')    






'''
Write a  Python program to find the largest k numbers from a given list of numbers.
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]

Try it with a for loop!
Is there a function in Python that will do this for us??

'''

test_list = [1, 2, 3, 4, 5, 5, 3, 6, 2]

max_number = max(test_list)
print(max_number)


'''
Please turn this:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

into this:
{'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
'''
# # My work
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # initialize variable
index = 0
output = ' '

# # loop
for letter in letters:
    index_and_letter = f" '{letter}': {index}, "
    output += index_and_letter
    index += 1
    
#     # output
print(output)