
def result_comparison():
    # val1 = 55
    # val2 = 60
    val1 = int(input("Enter the Val1 Value: "))
    val2 = int(input("Enter the Val2 Value: "))
    first_result = val1 + val2
    print(first_result)

    # val3 = 70
    # val4 = 45
    val3 = int(input("Enter the Val3 Value: "))
    val4 = int(input("Enter the Val4 Value: "))
    second_result = val3 + val4
    print(second_result)

    if first_result == second_result:
        print("Both the Results are similar")
    else:
        print("Both the Results are different")


result_comparison()
