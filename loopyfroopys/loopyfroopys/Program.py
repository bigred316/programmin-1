colors = ["red" , "green" , "blue"]
print(colors)
print(colors[2])
fruits = ["apple" , "banana", "orange" , "kiwi", "mango"]
print("")
#for-each loop
for item in fruits:
    print(item)
print("")
for index in range(len(fruits)):
    print(fruits[index])
print("")


lastfruit = fruits[len(fruits)-1]
# OR this only works in python
lastfruit = fruits[-1]
print(lastfruit)
input()
