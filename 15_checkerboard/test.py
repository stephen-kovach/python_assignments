
# I AM 15_CHECKERBOARD/TEST.PY

# ////////////////////////
# # STOPPED AT  YouTube Checkerboard Demo Part A 18:49
#         gonna try the lp instead


# ON THE VIDEO, List Demonstration was at: 
# YouTube Checkerboard Demo Part A 15:02

# [0, 1, 0],
# [1, 0, 1],
# [0, 1, 0]]

# from csv import list_dialects
# HEY------------Why did the above code just appear?  Similar ghost code on demo_10

# works with line  27
def generate_checkerboard(x, y):
    result = []  #result is a list of lists

    # print(x, y)
    
    for j in range(0, y):
        temp = []
        print = temp
        for i in range(0, x):
                temp.append((i + j) % 2)
            result.append(temp)
    
    return result

# # works with line 10
generate_checkerboard(6, 4)
generate_checkerboard(20, 700)


# BELOW IS IN THE TERMINAL:  WHY?
# 4 4 

#works with line 10, prints empty list
# print(generate_checkerboard(99, .07))
# print(generate_checkerboard(55, 4))


# BELOW IS IN THE TERMINAL:  WHY?
# 4 4 
# None        ISN'T THE LIST COMMENTED OUT?


# //////////COMPARE_Second Draft///////////////



# works with lines  66 [and] 74
# def generate_checkerboard(x, y):
#     # result = []  #result is a list of lists

#     print(x, y)
    
    # for j in range(0, y):
    #     temp = []
    #     print = temp
    #     for i in range(0, x):
    #             temp.append((i + j) % 2)
    #         result.append(temp)

            # print(x + y % 2)
    
    # return result

# works with line 49, no list
# generate_checkerboard(6, 4)
# generate_checkerboard(20, 700)


# BELOW IS IN THE TERMINAL:  WHY?
# 4 4 

#works with line 48, prints empty list
# print(generate_checkerboard(99, .07))
# print(generate_checkerboard(55, 4))


# BELOW IS IN THE TERMINAL:  WHY?
# 4 4 
# None        ISN'T THE LIST COMMENTED OUT?




# //////////COMPARE_First Draft///////////////

# BELOW IS IN THE TERMINAL:  WHY?
# 4 4 
# None        ISN'T THE LIST COMMENTED OUT?

# def generate_checkerboard(x, y):
#     # result = []  #result is a list of lists

#     print(x, y)
    
#     # for j in range(0, y):
#     #     temp = []
#     #     for i in range(0, x):
#     #             temp.append((i + j) % 2)
#     #         result.append(temp)

#             # print(x + y % 2)
    
#     # return result

# # generate_checkerboard(4, 4)
# print(generate_checkerboard(4, 4))
