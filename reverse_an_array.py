length_of_array = int(input("Enter number of elements: "))
input_array = []

for i in range(0, length_of_array):  # From 0 ... length_of_array - 1
    el = input("Enter the element:")
    input_array.append(el)

print("\nYour input:\n" + str(input_array))

input_array.reverse()
print("\nReverse array is:\n" + str(input_array))
