# from cs50 import get_string

# answer = get_string("What's your name? ")
# print(f"Hello, {answer}")

"""
print(f"Hello, {answer})
the f stands for "Formatted String" or "F Strings"
again {answer} is a variable.
the {answer} is a plug in value, taking what the user/system inputs
the {answer} works as a CHANGEABLE value when the f is in front of the "Hello, {}"
without the f it would print "Hello, {answer}" if we used the exact line above without the f. 
Feel free to try it to verify.
"""

answer = input("what's your name? ")
print(f"Hello, {answer}")

"""
Way to do the above code without the CS50 library.
"""