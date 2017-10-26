#Chapter 7 Strings-addtional-exercises number 1
def cap(x):
    x = x.title()
    return x

def initial(x):
    x = x[0]
    return x

firstName = input('Enter first name: ')
middleName = input('Enter middle name: ')
lastName = input('Enter last name: ')

firstName = cap(firstName)
middleName = cap(middleName)
lastName = cap(lastName)

fullName = firstName + ' ' + middleName + ' ' + lastName
print(fullName)

firstIn = initial(firstName)
middleIn = initial(middleName)
lastIn = initial(lastName)
initials = firstIn + '.' + middleIn + '.' + lastIn + '.'
print(initials)
