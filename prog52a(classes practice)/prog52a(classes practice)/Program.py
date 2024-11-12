class rectangle: 
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return self.length * 2 + self.width * 2

length = int(input("Enter length: "))
width = int(input("Enter width: "))
r = rectangle(length, width)
print("Area: " , r.area())
print("Perimeter: " , r.perimeter())
input()