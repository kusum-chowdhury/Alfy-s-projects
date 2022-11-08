# def calc_math_expression(num1, num2, operator):
#    if operator == "+":
#      print(num1 + num2)
#    elif operator == "-":
#      print(num1 - num2)
#    elif operator == "*": 
#      print(num1 * num2)
#    elif operator == "/" and num2 != 0:
#     print(num1 / num2)
#    else: 
#     print("None")

# calc_math_expression(5, 0, "/")

# def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
#     smallest = num1
#     largest = 0
#     if num1 > num2 and num1 > num3 :
#         largest = num1
#     elif num2 > num1 and num2 > num3:
#         largest = num2
#     else:
#         largest = num3
#     if num1 < num2 and num1 < num3:
#         smallest = num1
#     elif num2 < num1 and num2 < num3:
#         smallest = num2
#     elif num3 < num1 and num3 < num2:
#         smallest = num3
#     print(largest, smallest)

# find_largest_and_smallest_numbers(0, 10.01, 10)


def temp_checker(min_temp, temp_1, temp_2, temp_3):
    count = 0;       
    for x in temp_checker:
        if x != check:
            count+=1
            check = x
        
    if(count>1):
        return True

temp_checker(26, 38, 90, 20)

