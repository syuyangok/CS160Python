'''
Program7 : Part1: Ask user for new transactions and write to file; Part2: Display transactions from bank 
'''

# Part1: Ask user for new transactions and write to file
fileName = input ('Enter a file name: ')

outFile = open (fileName, 'w')

date = str(input('Enter a date(MM/DD/YY): '))
balance = float(input('Enter beginning balance: '))
balance = str(format(balance, '.2f'))

outFile.write(date + ',' + balance +'\n')

typ = str(input('Enter a type D(deposit)/W(withdraw) or Q/q to quit: '))

while typ.upper() != 'Q':
    date = str(input('Enter a date(MM/DD/YY): '))
    location = str(input('Enter a location: '))
    amount = float(input('Enter amount: '))
    amount = str(format(amount, '.2f'))
    typ = typ.upper()
    
    outFile.write(date + ',' + typ + ',' + location + ',' + amount + '\n')
    
    typ = str(input('Enter a type D(deposit)/W(withdraw) or Q/q to quit: '))

outFile.close()


#Part2: Display transactions from bank
print()
fileName = input ('Enter a file name to open: ')

inFile = open (fileName, 'r')

for line in inFile:
    line = line.rstrip()
    
    (date, value ) = line.split(',', 1)
    if value[0].isdigit():
        balance = float(value)
        print(format(date, '9s'), format('Beginning Balance', '25s'), format(balance, '45.2f'), sep='' )
        
    else:
        (typ, location, trans) = value.split(',')
        trans= float(trans)
        if typ.upper()== 'D':
            typ = 'Deposit'
            balance = float(balance + trans)
        elif typ.upper() == 'W':
            typ = 'Withdrawal'
            balance = float(balance - trans)
        
        print(format(date, '9s'), format(typ, '25s'), format(location, '15s'), format(trans, '15.2f'),format(balance, '15.2f'), sep='')

inFile.close()

