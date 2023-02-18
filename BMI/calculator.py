import importlib
#coded by laderhad
from formulas import calculate_BMI_USC
from formulas import calculate_BMI_SI
print()
print("1.imperial\n2.metric\n")
x = int(input("choose system(1 or 2):"))
if x == 1:
    lbs = float(input("lbs:"))
    inch = float(input("height:"))
    print(calculate_BMI_USC(lbs, inch))


elif x == 2:
    kg = float(input("kg:"))
    m = float(input("height:"))
    print(calculate_BMI_SI(kg,m))
else:
    print("please select 1 or 2")


    #coded by laderhad



