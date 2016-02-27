def calcualteLeftoverBalance(balance, fixedPayment, monthlyInterestRate):
    for month in range(1,13):
        #Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
        monthlyUnpaidBalance = balance - fixedPayment
    
        #Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        
    return balance

def sign(number):
    if (number > 0):
        return 1
    elif (number < 0):
        return -1
    else:
        return 0


#Monthly interest rate = (Annual interest rate) / 12.0
monthlyInterestRate = annualInterestRate / 12.0

#Monthly payment lower bound = Balance / 12
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance * ((1 + monthlyInterestRate)**12)) / 12.0

while True:
    
    instanceBalance = balance
    midPoint = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2
    
    midPointLeftoverBalance = calcualteLeftoverBalance(instanceBalance, midPoint, monthlyInterestRate)
        
    if (round(midPointLeftoverBalance, 2) == 0):
        print("Lowest Payment: " + str(round(midPoint, 2)))
        break;
    else:
        lowerPointLeftoverBalance = calcualteLeftoverBalance(instanceBalance, monthlyPaymentLowerBound, monthlyInterestRate)
        
        if(sign(lowerPointLeftoverBalance) == sign(midPointLeftoverBalance)):
            monthlyPaymentLowerBound = midPoint
        else:
            monthlyPaymentUpperBound = midPoint
            