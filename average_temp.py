temp=[]
no_of_days=int(input("Of how many days average temparature u want??\n"))
for i in range(0,no_of_days):
    per_day_temp=int(input(f"Give temperature of day "+str(i+1)+":"))
    temp.append(per_day_temp)

sum_of_temp=sum(temp)
avg=sum_of_temp/no_of_days
print(f"Average temparature is:"+str(avg))

above_avg_temp=0
for i in temp:
    if i>avg:
        print(f"Day "+str(i)+" had high temparature than average")
        above_avg_temp+=1

print(f"The no of days having temparature above average is "+str(above_avg_temp))


