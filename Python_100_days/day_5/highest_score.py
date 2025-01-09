# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# # print(range(1, 10))
# high_score = 0

# for score in student_scores:
#     if score > high_score:
#         high_score = score

# print(high_score)


# # range(1, 101)
# for number in range(1, 101):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
#     print(total)


# range(1, 101)
for number in range(1, 101):
    
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        
        
import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


rand_letters = random.choices(letters, k = nr_letters)
rand_symbols = random.choices(symbols, k = nr_symbols)
rand_numbers = random.choices(numbers, k = nr_numbers)
rand_letters.extend(rand_numbers)
rand_letters.extend(rand_symbols)
random.shuffle(rand_letters)
password = "".join([str(elem) for elem in rand_letters])
print(f"Your password is: ", password)        