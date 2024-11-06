
copies = int(input("Enter # of copies to print:"))
price = 0.0
cost = 0.0
 
if copies >0 and copies <= 99:
    price = 0.30
elif copies > 99 and copies >= 499:
    price = 0.28
elif copies > 499 and copies >= 749:
    price = 0.27
elif copies > 749 and copies >= 1000:
    price = 0.26
elif copies > 1000:
    price = 0.25
else:
    print("invalid # of copies")

cost = price * copies    
print("Total Cost is $" + str(round(cost , 2)))
input() #press enter to close only needed for sharpdevelop