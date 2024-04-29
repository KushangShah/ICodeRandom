# importing textwrap module which is python buildin module 
import textwrap

# def a function called wrap which takes two arrfument, string, max_width
def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, width=max_width))

# using __name__ and __main__ function to run the code
if __name__ == "__main__":
    string, max_width = str(input("Write string: ")), int(input("Enter number to wrap: "))
    output = wrap(string,max_width)
    print(output)

    