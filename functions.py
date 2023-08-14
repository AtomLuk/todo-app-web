FILEPATH = "todos.txt"  # constant


def get_todos(filepath = FILEPATH): # function reads it only, parameter
    # filepath = "todos.txt" and 1 arg
    #set it to a default argument
    """
    Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:  # don't need to close file
        todos_local = file_local.readlines()  #  local variable content read in this variable
    return todos_local
# print(help(get_todos))


def write_todos(todos_argument, filepath=FILEPATH): # parameters/arguments 2 arg
    """
    Write the to-do items list in the text file.
    """
    with open(filepath, 'w') as file:  # don't need to close file
       file.writelines(todos_argument)  # content read in this variable
# modify components so doesn't need to return
# todos_arg always changing so cannot be set equal to something


# print(__name__) # named function in import
if __name__ == "__main__":
    print("Hello")
    print(get_todos())


    # will only run this here but not when runned indirectly thru import