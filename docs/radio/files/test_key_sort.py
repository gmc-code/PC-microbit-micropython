# A function that returns the integer from a string:
def sort_int_strings(list_value):
    return int(list_value)

int_strings = ['5', '4', '6', '3']
int_strings.sort(key=sort_int_strings)
for int_str in int_strings:
    print(int_str, end=":")