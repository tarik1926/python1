def length_of_string(n):
    if n == "":
        return 0
    else:
        return 1 + length_of_string(n[1:])

n = input("Enter a string: ")
print("Length =", length_of_string(n))