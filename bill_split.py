bill = 87.93  #total bill
tip = 0.2     #20% tip
split = 3     #number of people

total = bill + (bill * tip ) # Calculate the total bill

each_pay = total / split     # Calculate what each person pays

print(each_pay)
print(round(each_pay,2))