print("Welcome to the Bill calculator: ")
bill=int(input("what was the total bill: $"))
tip=int(input("what percentage of tip would you like to give? 10, 12 or 15: ? "))
split=int(input("how many people to split the bill: "))
print(f"Each person should pay: ${round((bill+(bill*tip/100))/split,2)}")