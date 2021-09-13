user_input = int(input('Enter a number:'))
def pattern_1(user_input):
  
  for i in range(user_input+1):
    print('*'*i)
  print('\n')
pattern_1(user_input)

def pattern_2(user_input):
  for i in range(1,user_input+1):
    print('*'*user_input)
    user_input = user_input - 1
  print('\n')
pattern_2(user_input)

def pattern_3(user_input):
  for i in range(user_input+1):
    print(' '*(i)+'*'*(user_input-i))

    
pattern_3(user_input)

def pattern_4(user_input):
  for i in range(user_input+1):
    print(' '*(user_input-i)+'*'*i)
pattern_4(user_input)
