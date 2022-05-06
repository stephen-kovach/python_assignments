
# 1 Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1
x[1][0] =15
print(x)

# 2

# students[0]['last_name'] = 'Bryant'
# print(students)

# # 3

# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

# # 4

# z[0]['y'] = 30
# print(z)


# 2 Interate Through a List of Dictionaries


# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def interateDictionary(list):
#     for i in range(0, len(students)):
#         for key, val in students[i].items():
#             print(key, val)

# interateDictionary(students)

# interateDictionary(students):
#     for i in range(0, 4):
#         print(students[i])


# iterateDictionary(students)

# def iterateDictionary(some_list):
#     for current_dictionary in some_list:
#         for key, value in current_dictionary.items():
#             print(key, value) 

# iterateDictionary(students)

# we have four dictionaries in one list

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# 3 Get Values From a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def interateDictionary2(orange, banana):
#     for apple in banana:
#         for pear, kiwi in apple.items():
#             if(orange == pear):
#                 print(kiwi)

# interateDictionary2('first_name', students)
# interateDictionary2('last_name', students)


# def interateDictionary2(key_name, some_list):
#     for current_dictionary in some_list:
#         for key, value in current_dictionary.items():
#             if(key_name == key):
#                 print(value)

# interateDictionary2('first_name', students)
# interateDictionary2('last_name', students)



# 4. Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
#create a function
def printInfo(some_dict):
#print the length of each key
    for key, value in some_dict.items():
#print key name
        print(len(value), key)
# print values of each key
        for element in value:
            print(element)
            # print("\n", element)

# def iterateDictionary(some_list):
#     for current_dictionary in some_list:
#         for key, value in current_dictionary.items():
#             print(key, value) 



printInfo(dojo)


