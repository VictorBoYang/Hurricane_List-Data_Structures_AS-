from function_storage import *

# The language used is python3 #

# Ass 3
print("Assignment 3 Start...\n")
Storm1 = Storm("Tropical Storm Alberto", 60, "May", 0)
Storm2 = Storm("Tropical Storm Beryl", 70, "May", 0)
Storm3 = Storm("Hurricane Chris", 85, "June", 1)
Storm4 = Storm("Hurricane Ernesto", 100, "August", 2)
Storm5 = Storm("Hurricane Michael", 115, "September", 3)
double_linked_list = DoublyLinkedList()
double_linked_list.push_front(Storm1)
double_linked_list.push_back(Storm2)
double_linked_list.insert(Storm3, 1)
double_linked_list.push_front(Storm4)
double_linked_list.insert(Storm5, 2)
double_linked_list.print_Forward()
double_linked_list.print_Reverse()
double_linked_list.erase(1)
double_linked_list.print_Forward()
double_linked_list.print_Reverse()
print("Assignment 3 finished\n")

double_linked_list.push_back(Storm1)
double_linked_list.print_Forward()

# Ass 4
print("Assignment 4 Start...\n")
user_input = ""
while user_input is not None:
    user_input = input("Command: ")
    check_user_answer(user_input, double_linked_list)
    if user_input == "exit":
        user_input = None
        print("Exited")
