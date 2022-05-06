
# 1. Countdown

# ------mine

# array= []

# def countdown(x):
#     for x in range (x, -1, -1):
#         array.append(x)

# countdown(9)
# print(array)

# -------video


# def countdown(x):
#     array= []
#     for x in range (x, -1, -1):
#         array.append(x)
#     return array

# print(countdown(9))


# 2 Print and Return

# def print_and_return(list):

#     print(list[0])
#     return list[1]

# print(print_and_return([2, 3]))


# 3 First Plus Length

# def first_plus_length(list):
#     return list[0] + len(list)
    
# list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(first_plus_length(list))

# # which is better?  above or below?  If below, why do we not need to define the list?

# print(first_plus_length([1, 2, 3, 4, 5]))


# # 4 Values Greater Than Second

# def values_second(list):
#     if len(list) < 2:
#         return False
#     output = []
#     for i in range(0, len(list)):
#         if list[i] > list[1]:
#             output.append(list[i])
#     print(len(list))
#     return output

# print(values_second([1, 5, 3, 10, 4, 8, 9, 11]))
# print(values_second([2]))
# print(values_second([2, 1, 3]))

# # 5.  This length, that value

def value_length(size, value):
    output = []
    for i in range(0, size):
        output.append(value) 
    return output

print(value_length(4, 7))
print(value_length(6, 2))
print(value_length(8, 3))

