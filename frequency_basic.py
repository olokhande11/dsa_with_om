
def first_unique_char(s):
    for i in range(len(s)):
        current = s[i]
        count = 0
        for j in range(len(s)):
            if s[j] == current:
                count += 1
        if count == 1:
            print("First unique character is:", current)
            return
    print("No unique character found.")

input_str = input("Enter a string: ")
first_unique_char(input_str)