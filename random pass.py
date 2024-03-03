import random
symbollow = 'abcdefghijklmnopqrsyngwspuvzx'
number = '123456789'
symbolup = 'ABCDEFGHIJKLMNOPQRSYNGWSPUVZX'
symbol = '[](){}#@!$%^&*_-+=/|-'
ALL = symbol + symbollow + symbolup+number
length = 9
password =  "".join(random.sample(ALL,length))
print('password =',password)