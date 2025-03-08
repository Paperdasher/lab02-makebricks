#Examples how to call a method from a different Python file:

from function import test

# store it in a variable
x = test(1)

# print it
print(test(2))

# print it with context!
print("test(test(4)) =" + test(test(4)))


# The tests should print the intended output in addition to the actual output.
# You should also replace the placeholder text with an actual function call.

# print("makeBricks(1,1,2) expected false result: " + "REPLACE THIS")
# print("makeBricks(1,1,6) expected true  result: " + "REPLACE THIS" )


# Think of all the different possible cases, including edge cases
# Ex. large amount of big blocks, small amount of small blocks, true: makeBricks(4, 7, 24)

# This file will be checked as well to see if you are properly testing.
# Proper testing is important to ensure...
# 1. Your algorithm works
# 2. You can catch edge cases
# 3. Your code matches your algorithm