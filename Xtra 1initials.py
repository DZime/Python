def initials():
    name = input('Enter name: ')
    name_list = name.split()
    print(name_list)

    first = name_list[0][0]
    second = name_list[1][0]
    last = name_list[2][0]
    print(first.upper(),'.', second.upper(),'.', last.upper(),'.') 

initials()
