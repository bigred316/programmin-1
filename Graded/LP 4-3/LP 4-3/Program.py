eggs = float(input("How many eggs would you like? "))
price = 0
cost = 0 
if eggs > 0 and eggs < 48:
    price = float(0.50 / 12)
elif eggs >= 48 and eggs < 72:
    price = float(0.45 / 12)
elif eggs >= 72 and eggs < 132:
    price = float(0.40 / 12)
elif eggs >= 132:
    price = float(0.35 / 12)
else:
    print("Invalid Amount")



cost = price * eggs 
round(cost , 2)
print("Your eggs will cost $" + str(cost))
input()



