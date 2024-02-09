
prinipal = 55000 #p
rate = .05
numPayments = 60 #n
interestRate = (.05/12) #r

top = interestRate*(1+interestRate)**numPayments
bot = ((1+interestRate)**numPayments)-1

totalPaid =  round(((prinipal * (top/bot))*60), 2)
totalInter = totalPaid-prinipal

monthlyPay = round(prinipal * (top/bot),2)

lastPay = totalPaid-(monthlyPay*59)


print("The principal amount is: ", prinipal)
print("The interest rate is: ", rate)
print("The number of payments is:", numPayments)

print("Total amount paid: ", totalPaid)
print("Total interest paid: ", totalInter)

print("The monthly payment for the first 59 months is:", monthlyPay)
print("The last payment is:", round(lastPay,2))

