def num_2_word(char):
    if char == '0':
        print("Zero")
    elif char == '1':
        print("One")
    elif char == '2':
        print("Two")
    elif char == '3':
        print("Three")
    elif char == '4':
        print("Four")
    elif char == '5':
        print("Five")
    elif char == '6':
        print("Six")
    elif char == '7':
        print("Seven")
    elif char == '8':
        print("Eight")
    else:
        print("Nine")
char = input("Enter a character: ")
print(num_2_word(char), "\n")