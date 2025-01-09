import random
# import my_module

random_integer = random.randint(1, 10)
# print(random_integer)

# print(my_module.my_favorite_number)

if random_integer % 2 == 0:
    print("Heads")
else:
    print("Tails")
