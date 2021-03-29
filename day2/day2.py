print('Welcome to the tip calculator')
bill = float(input('What was the total bill? $'))
percentage = int(input('What percentage tip would you like to give? '))
split = int(input('How many people to split the bill? '))
eachPersonPay = (bill + (percentage * bill / 100)) / split
print(f'Each person must pay: ${round(eachPersonPay, 2)}')