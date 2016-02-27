#Monthly interest rate = (Annual interest rate) / 12.0
monthlyInterestRate = annualInterestRate / 12.0

coefficientMultiplier = 1

while True:
    
    instanceBalance = balance
    
    for month in range(1,13):
        #Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
        monthlyUnpaidBalance = instanceBalance - 10 * coefficientMultiplier
    
        #Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    
        instanceBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        
    if (instanceBalance <= 0):
        print ("Lowest Payment: " + str(coefficientMultiplier * 10))
        break;
    else:
        coefficientMultiplier += 1