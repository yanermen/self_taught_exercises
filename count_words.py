def count_word(input_string):
    if len(input_string.split(" ")) >= 2:
        split_str = input_string.split(" ")
        return len(split_str)
    else:
        return len(input_string)

print(count_word("Hello World"))
print(count_word("Hello"))
