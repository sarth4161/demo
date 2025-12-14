num=int(input("enter the numbers in list"))
ls=[]
for i in range(num):
  a=int(input("Enter the {}th number in the list".format(i)))
  ls.append(a)
choice=input("Do you want to search any number in list:[Y/N]:")[0]
if choice=='Y' or choice=='y':
    data=int(input("Enter the number do you want to search:"))
    cal=int((0+(num-1))/2)
    while(ls.index(data)!=ls[cal]):
        if(data<ls[cal]):
            firstindex=0;
            lastindex=cal
        elif(data>ls[cal]):
            firstindex=cal;
            lastindex=num-1;
        else:
            print("data found {}:".format(cal))
            break;
        cal=int((firstindex+lastindex)/2)
        

        
else:
    print("Thanks you:")
