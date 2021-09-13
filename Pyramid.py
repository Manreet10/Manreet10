user_input = int(input('Enter a number:'))
#Create 1st Pattern
def pattern_1(user_input):
  for i in range(user_input+1):
    print('*'*i)
  print('\n')
pattern_1(user_input)

#Create 2nd Pattern
def pattern_2(user_input):
  for i in range(1,user_input+1):
    print('*'*user_input)
    user_input = user_input - 1
  print('\n')
pattern_2(user_input)

#Create 3rd Pattern
def pattern_3(user_input):
  for i in range(user_input+1):
    print(' '*(i)+'*'*(user_input-i))
pattern_3(user_input)

#Create 4th Pattern
def pattern_4(user_input):
  for i in range(user_input+1):
    print(' '*(user_input-i)+'*'*i)
pattern_4(user_input)
