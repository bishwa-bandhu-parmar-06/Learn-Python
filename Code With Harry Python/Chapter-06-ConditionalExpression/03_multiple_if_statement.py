a = int(input("Enter Your age : "))

if(a % 2 == 0):
    print("Even Number")
# end of if satatement number 1 
if(a > 18):
    print("You are the above the age of consent.")
elif(a < 0):
    print("You are entering invalid age.")

elif(a == 0):
    print("You are a New Born Baby , Happy BirthDay")
else:
    print("You are not the above the age of consent.")
    
print("End of Program")