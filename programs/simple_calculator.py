# Simple calculator to perform arithmetic operations on two numbers.
# Allowed operations: +, -, *, /, %, ^


def main():
    print("What do you want to do?")

    print("\n1. Addition (+)")
    print("\n2. Subtraction (-)")
    print("\n3. Multiplication (*)")
    print("\n4. Division (/)")
    print("\n5. Modulus (%)")
    print("\n6. Exponentiation (^)")

    operator = int(input("Enter your choice: "))
    print("You chose: ", operator)
    validate_operator(operator)
    operands = take_inputs(operator)
    result = calculate(operator, *operands)
    # * operator can be used to unpack elements from an iterable (tuple in this case)
    print(result)


def calculate(operator, first_operand, second_operand):
    if not first_operand or not second_operand or not operator:
        print("Missing data to perform calculation!")
        return

    match operator:
        case 1:
            result = first_operand + second_operand
            result_string = str(first_operand) + " + " + str(second_operand) + " = "
        case 2:
            result = first_operand - second_operand
            result_string = str(first_operand) + " - " + str(second_operand) + " = "
        case 3:
            result = first_operand * second_operand
            result_string = str(first_operand) + " * " + str(second_operand) + " = "
        case 4:
            result = first_operand / second_operand
            result_string = str(first_operand) + " / " + str(second_operand) + " = "
        case 5:
            result = first_operand % second_operand
            result_string = str(first_operand) + " % " + str(second_operand) + " = "
        case 6:
            result = first_operand**second_operand
            result_string = str(first_operand) + " ^ " + str(second_operand) + " = "
            # ^ is used for bitwise XOR operation
            # pow(operator1, operator2) is same as operator1 ** operator2

    return "\nResult:\n" + result_string + str(result)


def validate_operator(operator):
    if not operator in range(1, 7):
        print("Invalid option!")


def take_inputs(operator):
    prompt1 = ""
    prompt2 = ""

    match operator:
        case 1:
            prompt1 = "First addend?"
            prompt2 = "Second addend?"
        case 2:
            prompt1 = "Minuend(number to subtract from)?"
            prompt2 = "Subtrahend(number that is subtracted)?"
        case 3:
            prompt1 = "Multiplicand?"
            prompt2 = "Multiplier?"
        case 4 | 5:
            prompt1 = "Dividend?"
            prompt2 = "Divisor?"
        case 6:
            prompt1 = "Base?"
            prompt2 = "Power?"
        case _:  # the catch-all pattern that does not match any values of previous cases
            print("Invalid choice!")
            return

    operand1 = int(input("\n" + prompt1 + " "))
    operand2 = int(input(prompt2 + " "))

    return operand1, operand2


main()
