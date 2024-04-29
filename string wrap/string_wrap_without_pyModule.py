# Without textwrap module we can perform the same system.

def wrap(string, max_width):
    wrapped_string = ""
    for i in range(0, len(string), max_width):
        wrapped_string += string[i:i+max_width] + "\n"
    return wrapped_string

# checking output
string = str(input("Enter the text here: "))
max_width = int(input("Enter the numbere here to wrap: "))
output = wrap(string, max_width)
print(output)