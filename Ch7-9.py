#Chapter 7 Strings-addtional-exercises number 9

x = input('Enter a string: ').lower()
print('You entered:', x)
numVow = x.count('a')
numVow = numVow + x.count('e')
numVow = numVow + x.count('i')
numVow = numVow + x.count('o')
numVow = numVow + x.count('u')
numVow = numVow + x.count('y')
print('Number of vowels:', numVow)
numCons = len(x) - numVow
print('Number of constenants:', numCons)
