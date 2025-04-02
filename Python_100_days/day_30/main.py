'''
try:  Something that might cause an exception

except: Do this if there was an exception

else: Do this if there were no exceptions

finally: Do this no matter what happens
'''

#FileNotFound 
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["dfsfge"])
# except FileNotFoundError:   #must include error type so other errors are NOT bypassed
#     file = open("a_file.txt", "w")  
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:        #when what you're trying succeeds
#     content = file.read()
#     print(content)
# finally:  #runs no matter what happens
#     file.close()
#     print("File was closed.")
# 
# new code 
# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)  


# Catch the exception and make sure the code runs without crashing.
# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndentationError:
#         print(f"Fruit pie")
#     else:
#         print(fruit + " pie")
# make_pie(4)
         
# Original code  Catch the exception and make sure the code runs without crashing.
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}   
# ]

# def count_likes(posts):
    
#     total_likes = 0
#     for post in posts:
#         total_likes = total_likes + post['Likes']
#     return total_likes    

# count_likes(facebook_posts)      

# above code with exception handling
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}   
]

def count_likes(posts):
    
        total_likes = 0
        for post in posts:
            try: 
                total_likes = total_likes + post['Likes']
            except KeyError:
                pass       
                   
        return total_likes    

count_likes(facebook_posts)   