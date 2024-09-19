code_string = 'hqz'


for character in code_string:
    ascii_num = ord(character)
    ascii_num -= 2
    new_char = chr(ascii_num)
    print(new_char, end="")

print()

code_string = 'ald'

for character in code_string:
    ascii_num = ord(character)
    ascii_num += 3
    new_char = chr(ascii_num)
    print(new_char, end="")

