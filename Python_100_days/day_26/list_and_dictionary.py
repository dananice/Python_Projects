'''numbers = [1, 2, 3]
new_list = []
for n in list:
    add_1 = n + 1
    
new_list.append(add_1)    

# to shorten the above code using list comprehension
# new_list = [new_item for item in list]

new_list = [n + 1 for n in numbers]

name = "Angela"
letters_list = [ letter for letter in name]

new_range = [n * 2 for n in range(1,5)]
'''

'''
# conditional list comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
cap_names = [name.upper() for name in names if len(name) > 5]


list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)
'''
'''
with open("file1.txt") as datafile1:
    file1 = datafile1.readlines()
    
with open("file2.txt") as datafile2:
    file2 = datafile2.readlines()

result = [int(num) for num in file1 if num in file2] 


print(result)
'''
'''
# dictionary comprehension
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {new_key:new_value for item in list}
students_scores = {student:random.randint(1, 100) for student in names}

# passed_students = {new_key:new_value for(key, value) in dictionary.items() if test }
passed_students = {student:score for(student, score) in students_scores.items() if score >= 60 }

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence.split()
result = {word:len(word.strip()) for word in sentence.split()}


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(temp * 9/5) + 32 for(day, temp) in weather_c.items()}

print(weather_f)

'''
student_dict = {
    "student": ["Angela","James", "Lily"],
    "score": [56, 76, 98]
}
# looping through DataFrame
import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)
    
# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)   # showing different ways to print info
    if row.student == "Angela":
        print(row)
        
        
# {new_key:new_value for (index, row) in df.iterrows()}