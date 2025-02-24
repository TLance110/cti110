#Trevor Deutsch
#2/23/25
#P1HW2
#program for basic travel budget


print('This program calculates and displays travel expenses\n\n')
#user inputs
budget = int(input('Enter Budget: '))
destination = input('\nEnter your travel destination: ')
gas = int(input('\nHow much do you think you will spend on gas? '))
sleep = int(input('\nApproximately, how much will you need for accomodation/hotel? '))
food = int(input('\nLast, how much do you need for food? '))
#add all expenses
expense = gas + sleep + food
#subtract from budget to get remaining balance
total = budget - expense
#summary output and total balance
print('\n\n------------Travel Expenses------------')
print('\nLocation:',destination,'\nInitial Budget:',budget)

print('\nFuel:',gas,'\nAccomodation:',sleep,'\nFood:',food)

print('\nRemaining Balance:',total)
