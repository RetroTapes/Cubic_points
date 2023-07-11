print("The transformations will be calculated in the given form (y = a√(b(x - h)) + k")

#Spacing
print("")
print("")

# Ask for all the 4 values
a_input = input("What is the value of a (leave blank if no 'a' is given): ")
if '/' in a_input:
    numerator, denominator = a_input.split('/')
    a = float(numerator) / float(denominator)
elif not a_input:
    a = 1.0
else:
    a = float(a_input)


b_input = input("What is the value of b (leave blank if no 'b' is given): ")
if '/' in b_input:
    numerator, denominator = b_input.split('/')
    b = float(numerator) / float(denominator)
elif not b_input:
    b = 1.0
else:
    b = float(b_input)


h_input = input("What is the value of h (leave blank if no 'h' is given): ")
if '/' in h_input:
    numerator, denominator = h_input.split('/')
    h = float(numerator) / float(denominator)
elif not h_input:
    h = 0
else:
    h = float(h_input)


k_input = input("What is the value of k (leave blank if no 'k' is given): ")
if '/' in k_input:
    numerator, denominator = k_input.split('/')
    k = float(numerator) / float(denominator)
elif not k_input:
    k = 0
else:
    k = float(k_input)

#Spacing
print("")
print("")


# Print all the transformations
print(f"a = {a}")
print(f"b = {b}")
print(f"h = {h}")
print(f"k = {k}")


print("")
print("")


#a reflection
if a > 0 :
    print("There is no reflection over the x-axis.")

else:
    print("There is a reflection over the x-axis")

#a vertical stretch
if abs(a) > 1:
    print(f"There is a vertical stretch by a factor of {abs(a)}")

elif abs(a) < 1:
    print(f"There is a vertical stretch by a factor of {abs(a)}")

elif abs(a) == 1:
    print("There is no vertical stretch.")

#spacing
print("")
print("")


#b reflection
if b > 0 :
    print("There is no reflection over the y-axis.")

else:
    print("There is a reflection over the y-axis")

#b horizontal stretch
if abs(b) > 1:
    print(f"There is a vertical stretch by a factor of {abs(b)}")

elif abs(b) < 1:
    print(f"There is a vertical stretch by a factor of {abs(b)}")

elif abs(b) == 1:
    print("There is no vertical stretch.")


#spacing
print("")
print("")

#h translations
if h > 0:
    print(f"{abs(h)} units to the left")
elif h < 0:
    print(f"{abs(h)} units to the right")
elif h == 0:
    print("No horizontal translations")
else:
    print('Invalid option chosen!')
    exit()

#spacing
print("")
print("")


#k translations
if k > 0:
    print(f"{abs(k)} units up")
elif k < 0:
    print(f"{abs(k)} units down")
elif k == 0:
    print("No vertical translations")
else:
    print('Invalid option chosen!')
    exit()

#spacing
print("")
print("")


#Points1
x1 = 0
x1_after = (x1 * (1/abs(b))) + -(h)
y1 = 0
y1_after = (y1 * a) + k

#Points2
x2 = 1
x2_after = (x2 * (1/abs(b))) + -(h)
y2 = 1
y2_after = (y2 * a) + k

#Points3
x3 = 4
x3_after = (x3 * (1/abs(b))) + -(h)
y3 = 2
y3_after = (y3 * a) + k

#Points4
x4= 9
x4_after = (x4 * (1/abs(b))) + -(h)
y4 = 3
y4_after = (y4 * a) + k

#Points5
x5 = 16
x5_after = (x5 * (1/abs(b))) + -(h)
y5 = 4
y5_after = (y5 * a) + k

#Points6
x6 = 25
x6_after = (x6 * (1/abs(b))) + -(h)
y6 = 5
y6_after = (y6 * a) + k

#Points7
x7 = 36
x7_after = (x7 * (1/abs(b))) + -(h)
y7 = 6
y7_after = (y7 * a) + k

#Points8
x8 = 49
x8_after = (x8 * b) + -(h)
y8 = 7
y8_after = (y8 * a) + k

#Points9
x9 = 64
x9_after = (x9 * b) + -(h)
y9 = 8
y9_after = (y9 * a) + k

#Points10
x10 = 81
x10_after = (x10 * (1/abs(b))) + -(h)
y10 = 9
y10_after = (y10 * a) + k

#Points11
x11 = 100
x11_after = (x11 * (1/abs(b))) + -(h)
y11 = 10
y11_after = (y11 * a) + k


#Printing all the points
#Printing all the points
print("The new points are:")
print(f"({x1_after},{y1_after})")
print(f"({x2_after},{y2_after})")
print(f"({x3_after},{y3_after})")
print(f"({x4_after},{y4_after})")
print(f"({x5_after},{y5_after})")
print(f"({x6_after},{y6_after})")
print(f"({x7_after},{y7_after})")
print(f"({x8_after},{y8_after})")
print(f"({x9_after},{y9_after})")
print(f"({x10_after},{y10_after})")
print(f"({x11_after},{y11_after})")


# Check for a 0 value in the y-coordinates
rows_with_zero = []
if y1_after == 0:
    rows_with_zero.append(1)
if y2_after == 0:
    rows_with_zero.append(2)
if y3_after == 0:
    rows_with_zero.append(3)
if y4_after == 0:
    rows_with_zero.append(4)
if y5_after == 0:
    rows_with_zero.append(5)
if y6_after == 0:
    rows_with_zero.append(6)

#spacing
print("")
print("")

# Print the row(s) with a 0 value
if rows_with_zero:
    print(f"The point(s) in row(s) {', '.join(map(str, rows_with_zero))} have a root.")
else:
    print("No roots found in the first 10 points.")