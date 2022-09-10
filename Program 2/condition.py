
#!With directly calling get_int
# from cs50 import get_int

# x = get_int("x: ")
# y = get_int("y: ")

# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")


#!WITHOUT directly calling get_int from CS50

import cs50 

#!cs50.(function) is called "Name-Spacing"

x = cs50.get_int("x: ")
y = cs50.get_int("y: ")

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")