w=float(input("Enter your weight in Kg: "))
h=float(input("Enter your height in cm: "))
bmi=w/(h/100)**2
if bmi<=18.4:
    print("You are underweight!")
elif 18.4<bmi<=24.4:
    print("You are healthy!")
elif 24.4<bmi<=29.4:
    print("You are overweight!")
elif 29.4<bmi<=34.4:
    print("You are Obese!")
else:
    print("Invalid input!")
    

