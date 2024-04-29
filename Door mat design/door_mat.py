# Defing a fuction that take two parameter 
def create_door_mat(rows,columns):
    # calculate the center of index for WELCOME text.
    center_index = columns//2

    # using for loop to range over num
    for i in range(rows//2):
        patterns = ".|." * (2 * i + 1)
        print(patterns.center(columns, "-"))

    # print welcome message
    print("WELCOME".center(columns, "-"))

    # reverse the top process
    for i in range(rows//2 -1, -1, -1):
        patterns = ".|." * (2 * i + 1)
        print(patterns.center(columns, "-"))

# using __ method to get input and print out result
if __name__ == "__main__":
    n, m = map(int,input().split())
    output = create_door_mat(n,m)
    print(output)

#  ignore the none message in the end