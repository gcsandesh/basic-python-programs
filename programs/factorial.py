""" To find the factorial of a number """


def find_factorial(num):
    if num == 0:
        return 1
    else:
        return num * find_factorial(num - 1)


def validate_input(n):
    is_valid = False
    if n < 0:
        print("Number is negative.\nFactorial does not exist.")
    # elif r"$[0-9]+".match(n):
    #     print("is not a number")
    else:
        is_valid = True

    return is_valid


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if validate_input(number):
        factorial = find_factorial(number)
        print(factorial)
