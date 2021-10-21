# Emily Catanzariti, Angel Scott, Tim Hunt
# CS 151, Dr. Rajeev
# 10/21/2021
# Lab 5
# Inputs: floor type, length and width of floor for each of the five rooms
# Outputs: total cost of floor type

# define floor type


def floor_type():
    type = input("What floor type would you like? hardwood, carpet, or tile?")
    type = type.strip().lower()
    if type == "hardwood":
        cost_per_sqft = 1.39
    elif type == "carpet":
        cost_per_sqft = 3.99
    elif type == "tile":
        cost_per_sqft = 4.99
    else:
        print("Sorry, your input is invalid. The cost of this room will be $0")
        cost_per_sqft = 0
    return cost_per_sqft


# define area


def area(length, width):
    length = float(length)
    width = float(width)
    area = length * width
    return area


# define room function
def room():
    cost_of_type = floor_type()
    length = input("What is the length of your room in feet?")
    width = input("What is the width of your room feet?")
    area_of_room = area(length, width)
    cost_of_room = cost_of_type * area_of_room
    return cost_of_room

# define main
def main():
    room1 = room()
    print("The cost of your first room is $%.2f" % room1)
    room2 = room()
    print("The cost of your second room is $%.2f" % room2)
    room3 = room()
    print("The cost of your third room is $%.2f" % room3)
    room4 = room()
    print("The cost of your fourth room is $%.2f" % room4)
    room5 = room()
    print("The cost of your fifth room is $%.2f" % room5)
    total_cost = room1 + room2 + room3 + room4 + room5
    print("The total cost of all of your rooms is $%.2f" % total_cost)


main()
