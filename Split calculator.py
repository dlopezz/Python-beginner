# Split calculator
print("Welcome to the tip calculator")
total = input("What was the total bill? $")
new_total = float(total)
people = input("How many people to split the bill? ")
new_people = int(people)
percentage = input("What percentage tip would you like to give? 10,12, or 15? ")
int_percentage = int(percentage)
if int_percentage == 10:
     int_percentage =(new_total*0.10)
elif int_percentage == 12:
     int_percentage =(new_total*0.12)
elif int_percentage == 15:
     int_percentage =(new_total*0.15)
else :
    print("no es correcto")  
total_tip =new_total+int_percentage
bill_split = total_tip/new_people
#new_bill_split = str(bill_split)
round_bill_split =round(bill_split,2)
new_round_bill_split = str(round_bill_split)
print("Each person should pay: $" + new_round_bill_split)