#spam = 0
#while spam < 5:
#    print('Hello, World.')
#    spam = spam + 1

# type your name
#name = ''
#while name != 'your name':
#    print('Please type your name. ')
#    name = input()
#print('Thank you!')

# break statement
#while True:
#    print('Please type your name.')
#    name = input()
#    if name == 'your name':
#        break
#print('Thank you!')

# continue statement
#while True:
#    print('Who are you?')
#    name = input()
#    if name != 'Joe':
#        continue
#    print('Hello Joe. What is the password? (is it a fish)')
#    password = input()
#    if password == 'swordfish':
#        break
#print('Access granted.')

# loops and range function
print('My name is')
for i in range(5):
    print('Jimmy five times (' + str(i) + ')')

# Add 1 - 100
total = 0
for num in range(101):
    total = total + num
print(total)
