monthlyInterestRate = annualInterestRate / 12.0

#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
minimumMonthlyPayment = monthlyPaymentRate

#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

totalPaid = 0;

for month in range(1,13):
    
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    totalPaid += minimumMonthlyPayment;
    
    print ("Month: " + str(month))
    print ("Minimum monthly payment: " + str(round(minimumMonthlyPayment, 2)))
    print ("Remaining balance: " + str(round(balance, 2)))
    
print ("Total paid: " + str(round(totalPaid, 2)))
print ("Remaining balance: " + str(round(balance, 2)))