from Node import *


def check_if_valid_month(user_input_month, double_linked_list):
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November", "December"]
    if user_input_month in month:
        double_linked_list.linear_search_month(user_input_month)
    elif user_input_month not in month:
        print("Invalid Month")


def check_user_answer(user_input, double_linked_list):
    if user_input == "sortwind":
        double_linked_list.bubble_sort_list()
        double_linked_list.print_Forward()
    elif user_input == "searchname":
        user_input_name = input("Enter Name: ")
        double_linked_list.linear_search_name(user_input_name)
    elif user_input == "searchcategory":
        user_input_category = input("Enter Category: ")
        user_input_category = int(user_input_category)
        double_linked_list.linear_search_category(user_input_category)
    elif user_input == "searchmonth":
        user_input_month = input("Enter Month: ")
        check_if_valid_month(user_input_month, double_linked_list)
    elif user_input == "exit":
        pass
    else:
        print("Invalid Command")
