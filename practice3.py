print(7+4)
print("Marty" + "De Alba") 
print(type(144))
print(type("Marty"))
print(type(6.9))
length = 3
width = 6
area = length * width
print(area) 


bill = 47.28
tip = bill * .15
total = bill + tip
share = total / 2
print("Each person needs to pay: " + str(share))

#print("2 + 2 = " + "2 + 2")

def greeting(name, department):
    print("Welcome, " + name + ".")
    print("You are joining " + department + "!")
greeting("Harry Potter ", "Global Technical Support") 

greeting("Bobby Bonilla", "New York Mets")

print("") 
def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3) 
sum = area_a + area_b
print("the sum of both areas is: " + str(sum))
