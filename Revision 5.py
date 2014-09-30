#Indi Knighton
#23/09/2014
#Revision task 5

lift_height = float(input("Please enter the height of a lift: "))
lift_width = float(input("Please enter the width of a lift: "))
lift_depth = float(input("Please enter the depth of a lift: "))

fridge_height = lift_height/2
fridge_width = lift_width/3
fridge_depth = lift_depth/1.5

height_remaining = lift_height - fridge_height
width_remaining = lift_width - fridge_height
depth_remaining = lift_depth - fridge_depth

print("Inside the lift there is {0} meters of height remaining. {1} of width remaining and {2} of depth remaining.".format(height_remaining, width_remaining, depth_remaining))
