def prime_checker(num):
    i=2
    k=0
    while(num>=i):
        if num%i==0:
            k+=1
        i+=1

    if k==1:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")


n=int(input("Enter a number:"))
prime_checker(n)
