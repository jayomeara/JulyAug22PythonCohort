def countdown(num):
    for i in range (num,0,-1):
        print (i)

countdown(10)

def print_and_return(num1,num2):
    print(num1)
    return(num2)

print_and_return(10,5)

def first_plus_length(list):
    sum = (list[0]+len(list))
    # print(len(list))
    print(f"first value:",sum,"+ length:",len(list))

first_plus_length([1,2,3,4,5]) 



# def values_greater_than_second(list):
#     newlist = []
#     for y in range(list):
#         if y>= list[1]:
#             newlist.append[y]
#         else:
#             return


# values_greater_than_second([5,2,3,2,1,4])


def length_and_value(num3,num4):
    newlist2 = []
    length = num4
    value = num3
    newlist2.append(str(length) * value)
    print(newlist2)

length_and_value(6,2)