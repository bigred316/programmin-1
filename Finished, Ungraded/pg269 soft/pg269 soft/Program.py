discountA = 1
discountB = 1
discountC = 1
pkA = input("What quantity would you like to purchase package A in?")
pkB = input("What quantity would you like to purchase package B in?")
pkC = input("What quantity would you like to purchase package C in?")
if float(pkA) < 10:
    discountA = 1
elif float(pkA) in range (10, 20):
    discountA = 0.8
elif float(pkA) in range (20, 50):
    discountA = 0.7
elif float(pkA) in range (50, 99):
    discountA = 0.6
else:
    discountA = 0.5

if float(pkB) < 10:
    discountB = 1
elif float(pkB) in range (10, 20):
    discountB = 0.8
elif float(pkB) in range (20, 50):
    discountB = 0.7
elif float(pkB) in range (50, 99):
    discountB = 0.6
else:
    discountB = 0.5
    
if float(pkC) < 10:
    discountC = 1
elif float(pkC) in range (10, 20):
    discountC = 0.8
elif float(pkC) in range (20, 50):
    discountC = 0.7
elif float(pkC) in range (50, 99):
    discountC = 0.6
else:
    discountC = 0.5
    
priceA = (float(pkA) * 99) * discountA
priceB = (float(pkB) * 199) * discountB
priceC = (float(pkC) * 299) * discountC
print("Package A= " + str(priceA))
print("Package B= " + str(priceB))
print("Package C= " + str(priceC))
print("Grand total= " + str(priceA+priceB+priceC))
input()
