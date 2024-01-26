# Weight converter

weight = input('Enter your weight:')
weight = float(weight)

weight_unit = input('(L)bs or (K)g:')

if weight_unit.lower() == 'l':
    weight = weight * 0.453592
    target_unit = 'Kg'
    print("Your weight in " + target_unit + " is: " + str(weight))
elif weight_unit.lower() == 'k':
    weight = weight * 2.20462
    target_unit = 'Lbs'
    print("Your weight in " + target_unit + " is: " + str(weight))
else:
    print("Invalid choice. Please try again!")