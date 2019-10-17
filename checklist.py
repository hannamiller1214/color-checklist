checklist = list()

# Create
def create(item):
    checklist.append(item)

# Read
def read(index):
    return checklist[int(index)]

# Update
def update(index, item):
    checklist[index] = item

# Destroy
def destroy(index):
    checklist.pop(index)

#List All Items
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# Mark Completed
# def mark_completed(index):


# Select
def select(function_code):
    if function_code.lower() == "a":
        input_item = user_input("Add to list: ")
        create(input_item)

    elif function_code.lower() == "r":
        item_index = user_input("Index Number? ")
        print(read(item_index))

    elif function_code.lower() == "p":
        list_all_items()

    elif function_code.lower() == "u":
        list_all_items()
        item_index = user_input("Number of item to update? Press X to cancel: ")
        if item_index.lower() == "x":
            return False
        input_item = user_input("Enter updated item: ")
        input_item = str(input_item)
        update(item_index, input_item)
        list_all_items()

    elif function_code.lower() == "d":
        list_all_items()
        item_index = user_input("Number of item to destroy? Press X to cancel: ")
        item_index = int(item_index)
        destroy(item_index)
        list_all_items()
#Look at how to globally run
    elif function_code == "Q":
        return True
    else:
        print("Unknown Option")
    return True


# User Input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# Test
# def test():
#     create("purple sox")
#     create("red sox")
#
#     print(read(0))
#     print(read(1))
#
#     update(0, "purple sox")
#
#     destroy(1)
#
#     print(read(0))
#
#     select("C")
#
#     list_all_items()
#
#     user_value = user_input("Please Enter a value:")
#     print(user_value)
#
# test()

running = True
while running:
    selection = user_input(
        "Press A to add to list, R to Read from list, U to Update item, D to Destroy item, P to display list, and Q to quit > ")
    running = select(selection)
