# Exercise 8
# An online retailer sells two products: widtets and gizmos.
# Each widget weighs 75 grams. Each gizmo weighs 112 grams.
# Write a program that reads the number of widgets and the number of gizmos from the user.
# Then your program should compute and display the total weight of the parts.

widget_weight = 75
gizmo_weight = 112

widget_count = int(input("How many widgets do you have? "))
gizmo_count = int(input("How many gizmos do you have? "))

weight = widget_weight * widget_count + gizmo_weight * gizmo_count

print("The total weight is", weight, "grams.")