prinipal = 55000#int(input("Principal amount: "))            #p
rate = .05#float(input("Interest Rate (APR): "))
numPayments = 60#int(input("Monthly Payments: "))            #n
interestRate = (rate/12)     #r

top = interestRate*((1+interestRate)**numPayments)
bot = ((1+interestRate)**numPayments)-1

cumPayment =  round((prinipal * (top/bot))*(numPayments),2)        #the total amount paid by the end
totalInterestPaid = cumPayment-prinipal                     #the total interst paid by the end

monthlyPayment = round(prinipal * (top/bot),2)             #the monthly payment            #A

balanceOwed = prinipal      #the balanced still owed at the end of each month   #B


print("Month\t| Monthly Payment    \t| Interest    \t| Prinipal    \t| Remaining Balance")



for i in range (1, numPayments):

    
    monthlyInterest = round(balanceOwed * interestRate, 2)                    #the part of the montly payment that is due too interest
    monthlyPrincipal = round(monthlyPayment - (balanceOwed*interestRate), 2)           #the part of the monthly payment that goes towards the principal
    balanceOwed = round(balanceOwed - monthlyPayment + monthlyInterest, 2)        #the updated balanced owned after every payment, including interest
    

    print(i, "   \t|", monthlyPayment, "   \t\t|", monthlyInterest,  "   \t|", monthlyPrincipal, "   \t|", balanceOwed)




finalInterest = monthlyPrincipal * interestRate         #the amount paid in interest for the last payment
finalPayment =  finalInterest + balanceOwed      #the payment for the last payment, including any rounding
monthlyPrincipal = balanceOwed
finalBalance = balanceOwed - finalPayment +  finalInterest


print(numPayments, "   \t|", round(finalPayment, 2), "   \t\t|", round(finalInterest, 2),  "   \t|", round(monthlyPrincipal, 2), "   \t|", round(finalBalance, 2))

