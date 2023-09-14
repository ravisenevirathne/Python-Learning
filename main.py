# print("Hello"+" World")
# print(5-2)
# print(f"10 days are {10*24*60*60}  seconds")
#

# print(f"10 days are {10 * calculations_to_seconds} {name_of_unit}")
# print(f"20 days are {20 * calculations_to_seconds} {name_of_unit}")
# print(f"200 days are {200 * calculations_to_seconds} {name_of_unit}")


# def scope_check(num_of_days):
#     my_var = "variable inside function"
#     print(name_of_unit)
#     print(num_of_days)
#     print(my_var)
#
#
# scope_check(1000)
#################################################################################################

# calculations_to_seconds = 24 * 60 * 60
# name_of_unit = "seconds"
#
#
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * calculations_to_seconds} {name_of_unit}"
#
#
# def validate_and_execute():
#     if user_input.isdigit():   # checking for only positive full numbers
#         user_input_number = int(user_input)
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print("you entered Zero, Please enter valid positive number ")
#     else:
#         print("Please enter valid positive number")
#
#
# user_input = input("Enter number of days and I will convert it to seconds : \n")
# validate_and_execute()
#################################################################################################

calculations_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculations_to_seconds} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered Zero, Please enter valid positive number ")
        else:
            print("You entered a negative number, Please enter valid positve number")
    except:
        print("Please enter valid positive number")


user_input = input("Enter number of days and I will convert it to seconds : \n")
validate_and_execute()


