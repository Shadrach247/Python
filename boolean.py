# The "AND" operator
print(True and True)
print(True and False)

# "AND" Truth Table
#True and True = True
#True and False = False
#False and True = False
#False and False = False

# The "OR" operator
print(False or True)
print(False or False)

# "OR" False Table
#True or True = True
#True or False = True
#False or True = True
#False or False = False


# The "NOT" operator
#not True = False
#not not not not True = True

# "NOT" Truth Table
print(not True)
print(not False)

# Mixing Boolean and Comparism operators
print(4 < 5) and (5 < 6)
print(4 < 5) and (9 < 6)
print(1 == 2) or (2 == 2)

# The Boolean operators have an order of operations just like the math operators do. 
# After any math and comparism operators evaluate, Python evaluates the "not" operators first, 
# then the "and" operators, and then the "or" operators.