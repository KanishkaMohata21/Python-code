height=input("Enter your height\n")
weight=input("Enter your weight\n")
result=round(int(weight)/float(height)**2)
print("Your BMI result is "+ str(result))

if result<18.5:
    print("You are underweight")
elif result<25:
    print("You have normal weight")
elif result<30:
    print("You are Overweight")
elif result<35:
    print("You are Obese")
else:
    print("You are CLINICALLY Obese")


