def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_loc = [a + apple for apple in apples]
    orange_loc = [b + orange for orange in oranges]

    apples_on_house = 0
    oranges_on_house = 0

    for apple in apple_loc:
        if apple >= s and apple <= t:
            apples_on_house += 1
    for orange in orange_loc:
        if orange >= s and orange <= t:
            oranges_on_house += 1

    print(str(apples_on_house) + "\n" + str(oranges_on_house))


if __name__ == "__main__":
    first_row_input = input("Enter start and end of house: ").strip().split()

    s = int(first_row_input[0])  # house start
    t = int(first_row_input[1])  # house end

    second_row_input = (
        input("Enter location of apple tree and orange tree: ").strip().split()
    )
    a = int(second_row_input[0])  # apple tree
    b = int(second_row_input[1])  # orange tree

    third_row_input = input("Enter number of apples and oranges: ").strip().split()
    apples_count = int(third_row_input[0])  # no. of apples
    oranges_count = int(third_row_input[1])  # no. of oranges

    apples = list(
        map(int, input("Enter distances where apples fall: ").strip().split())
    )
    oranges = list(
        map(int, input("Enter distances where oranges fall: ").strip().split())
    )
    countApplesAndOranges(s, t, a, b, apples, oranges)

# SAMPLE INPUT

# 7 11
# 5 15
# 3 2
# -2 2 1
# 5 -6

# SAMPLE OUTPUT
# 1
# 1
