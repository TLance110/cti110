#Trevor Deutsch
#2/23/25
#P1HW1
#code to collect user info process that info and output the result

print('-----Calculating Exponents----\n\n\nEnter an integer as the base value: ', end='')
ExInt1 = int(input())
ExInt2 = int(input('Enter an integer as the exponent: '))
ExSol = ExInt1 ** ExInt2
print('\n')
print(ExInt1,'raised to the power of', ExInt2,'is', ExSol,'!!')


print('\n\n-----Addition and Subtraction----\n\n\nEnter a starting integer:',end=' ')
StartInt = int(input())
AddInt = int(input('Enter an integer to add: '))
SubInt = int(input('Enter an integer to subtract: '))
ASSol = StartInt + AddInt - SubInt
print('\n')
print(StartInt,'+',AddInt,'-',SubInt,'is equal to',ASSol)
