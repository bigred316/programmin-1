flag = 0
calories = float(input("Please enter the amount of calories in your food: "))
fat = float(input("Please enter the amount of fat, in grams, in your food: "))
if fat <= 0 and calories <= 0:
    pass
else:
    fatcalories = fat * 9
    if fatcalories > calories:
        messageBox.Show("You cant have more fat calories than total calries, and as such, your input must be incorrect")
        pass
    else:
        percentfat = 100*(fatcalories/calories)
        if percentfat <= 30:
            flag = 1
        print(str(percentfat) +"% of the calories in your food come from fat.")
        if flag == 1:
            print("Your food is low in fat")
        input()