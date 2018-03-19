a=int(input("enter the number 1"))
    b=int(input("enter the number 2"))
    c=int(input("enter the number 3"))
    if(a>=b and a>=c):
        largest=a
    elif(b>=a and b>=c):
        largest=b
    else:
        largest=c
    print("The largest number between",a,",",b,"and",c,"is",largest)
