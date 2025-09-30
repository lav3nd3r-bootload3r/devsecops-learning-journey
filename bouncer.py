#ask for age
#age = input("How old are you? ")
#if age:
#    age = int(age)
#    if age >= 18 and age < 21:
#        print("You can enter, but you need a wristband!")
#    # 18-21 wristband
#    #21+ drink, normal entry
#    elif age >= 21:
#        print("You can enter and drink!!")
#    # too young, sorry
#    else: 
#        print("You are not old enough to enter!")   
#else: 
#    print("Please enter your age to continue")  


age = input("How old are you? ")
if age:
    age = int(age)
    if age >= 21:
        print("You are good to enter and drink!")
    elif age >= 18:
        print("You can enter, but you need a wristband!")
    else: 
        print("You are not old enough to enter!")   
else: 
    print("Please enter your age to continue")  
