temp=float(input("Enter Temperature : "))
unit=input("Enter Unit \nCelsius for 'C' & Fahrenheit for 'F'\nPlease Enter Capital Letters : ")
if unit=="C":
    tempf=temp*(9/5)+32
    print(tempf)
elif unit=="F":
    tempc=(temp-32)*(5/9)
    print(tempc)
else:
    print("Invalid Unit")