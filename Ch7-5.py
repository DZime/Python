#Chapter 7 Strings-addtional-exercises number 5

phone = input('Enter a 10 digit phone number using the format XXX-XXX-XXXX: ')
phone = phone.upper()
print(phone)

transPhone = phone.replace('A', '2').replace('B', '2').replace('C', '2')
transPhone = transPhone.replace('D', '3').replace('E', '3').replace('F', '3')
transPhone = transPhone.replace('G', '4').replace('H', '4').replace('I', '4')
transPhone = transPhone.replace('J', '5').replace('K', '5').replace('L', '5')
transPhone = transPhone.replace('M', '6').replace('N', '6').replace('O', '6')
transPhone = transPhone.replace('P', '7').replace('Q', '7').replace('R', '7').replace('S', '7')
transPhone = transPhone.replace('T', '8').replace('U', '8').replace('V', '8')
transPhone = transPhone.replace('W', '9').replace('X', '9').replace('Y', '9').replace('Z', '9')
print(transPhone)
