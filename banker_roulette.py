import random
names_string=input("Give me everybody's name separated by a comma:")
names=names_string.split(",")

length=len(names)
num=random.randint(0,length-1)

print(names[num]+" has to pay the bill")



