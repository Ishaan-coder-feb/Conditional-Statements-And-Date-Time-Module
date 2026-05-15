wd=int(input("Enter the total number of working days in your acadamic year: "))
pd=int(input("Enter the total number of days you were present in your acadamic year: "))
h=input("Do you have a medical restriction? Respond with yes or no : ")
p=(pd/wd)*100
if h=="no" or "No":
    if p > 80:
        print("Yoo do not have any medical restrictions and have an attendace percentage of above 80,so you can attend the exam.Yay!")
    else:
        print("You attandance is below the acceptable mark.Sorry!You cannot attend the exam!")
else:
    print("Due to health restrictions you cannot write th exam!")