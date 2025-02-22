import math

#1
def degree_to_radian():
    degree = float(input("Input degree: "))
    radian = degree * (math.pi / 180)
    print("Output radian:", round(radian, 6))
    return radian

degree_to_radian()



#2
def trapezoid_area():
    height = float(input("Height: "))
    base1 = float(input("Base, first value: "))
    base2 = float(input("Base, second value: "))
    area = 0.5 * (base1 + base2) * height
    print("Expected Output:", area)
    return area

trapezoid_area()



#3
def regular_polygon_area():
    n = int(input("Input number of sides: "))
    s = float(input("Input the length of a side: "))
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    print("The area of the polygon is:", round(area, 2))
    return area

result = regular_polygon_area()



#4
def parallelogram_area():
    base = float(input("Length of base: "))
    height = float(input("Height of parallelogram: "))
    area = base * height
    print("Expected Output:", area)
    return area

result = parallelogram_area()



