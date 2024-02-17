inputValue1=int(input("Enter your 1st number of choice : "))
inputValue2=int(input("Enter your 2nd number of choice : "))
answer=1
for p in range(1,inputValue2+1):
    answer =answer * inputValue1

    print("The power of ",inputValue2,"of",inputValue1," is : ",answer)