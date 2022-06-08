

# grade = 8.8
# age = 25

# print( age )

# name = "Zen"
# print("My name is", name)

# # print("Hello" + 42)			# output: TypeError
# print("Hello" + str(42))		# output: Hello 42


# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")

# List

# drawer = ['documents', 'envelopes', 'pens']
# #access the drawer with index of 0 and print value
# print(drawer[0])  #prints documents
# #access the drawer with index of 1 and print value
# print(drawer[1]) #prints envelopes
# #access the drawer with index of 2 and print value
# print(drawer[2]) #prints pens



# x = [1,2,3,4,5]
# x.append(99)
# print(x)
# #the output would be [1,2,3,4,5,99]

# Loops

for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

# If we want to interate though a ist we could use the range function and send in the length of the list as the stopping value

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

