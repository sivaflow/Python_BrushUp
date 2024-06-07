import math
def area_calculator(shape, size):
    if shape =="circle":
        radius = size[0]
        return math.pi *(radius**2)
    elif shape == "rectangle":
        length,breadth=size
        
        return length * breadth
    else:
        return "invalid"
circle_area = area_calculator("circle",(14,))
rectangle_area = area_calculator("rectangle",(10,20))
print(f"Rectangle area: {rectangle_area}")
print(f"Circle area: {circle_area}")