print("WELCOME TO TIP CALCULATOR\n")
total=float(input("What is your total bill?\n"))
percentage=int(input("What percentage tip would you like to give?,10,12 or 15?\n"))
tip=total*percentage/100
amount=total+tip
noOfPerson=int(input("How many people to split the bill\n"))
splitAmount=amount/noOfPerson
finalAmount=round(splitAmount,2)
print("Each person has to pay:"+str(finalAmount))