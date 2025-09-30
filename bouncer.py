#ask for age
age = input("How old are you? ")

if age >= "18" and age < "21":
    print("You can enter, but you need a wristband!")
# 18-21 wristband
#21+ drink, normal entry
elif int(age) >= 21:
    print("You are good to go!!")
# too young, sorry
else: 
    print("You are not old enough to enter!")   
    