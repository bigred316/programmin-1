print ("Can we deliver it?")
kiloyn = 0 #the variable name has a purpose i SWEAR
volyn = 0
weight = int(input("Enter weight of package in kilograms:"))
length = int(input("Enter length of package in centimeters:"))
height = int(input("Enter height of package in centimeters:"))
width = int(input("Enter width of package in centimeters:"))
vol = weight * length * height
if weight > 27:
    kiloyn = 1
if vol > 100000:
    volyn = 1
if volyn == 0 and kiloyn == 0:
    print("We can ship it!")
elif volyn == 0 and kiloyn == 1:
    print("Your package is too heavy")
elif volyn == 1 and kiloyn == 0:
    print("Your package is too large")
else:
    print("Your package is too heavy and too large")
input()
    
