import re

def name_function():
    valid = False
    valid_length = False
    valid_num = False
    valid_symbol = False

    while valid == False:
        full_name = input("Insert name:")

        if len(full_name) <= 35 and len(full_name) >= 1:
            valid_length = True
        else:
            if len(full_name) > 35:
                print("Name provided is too long")

            else:
                print("Name provided is too short")

            valid_length = False

        for char in full_name:
            if char.isdigit():
                print("Name provided includes digits")
                valid_num = False
                break

            else:
                valid_num = True

        string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (string_check.search(full_name) == None):
            valid_symbol = True

        else:
            print("Name provided includes special characters")
            valid_symbol = False

        if valid_num and valid_symbol and valid_length:
            for char in full_name:
                if char == '"':
                    print("Name provided includes special characters")
                    print("Name is invalid")
                    valid = False
                    break

                else:
                    valid = True

            if valid == True:
                print("Name is valid")

        else:
            print("Name is invalid")
            valid = False


def date():
    valid_data = False
    dic_month = {31:[1,3,5,7,8,10,12], 30:[9,4,6,11]}

    valid_day = False
    valid_month = False
    valid_year = False

    while valid_data == False:
        data = input("Date:")
        day = int(data[0:2])
        month = int(data[3:5])
        year = int(data[6:10])

        if year >= 1 and year <= 2009:
            valid_year = True
            if day == 31:
                if month in dic_month[30]:
                    valid_day = False

            elif day > 31 or day < 1:
                valid_day = False

            else:
                valid_day = True

        else:
            valid_year = False

        if month >= 1 or month < 13:
            valid_month = True
            if month == 2:
                if day == 29:
                    if year % 4 == 0:
                        valid_month = True
                    else:
                        valid_month = False

        else:
            valid_month = False

        if valid_month == True and valid_day == True and valid_year == True:
            valid_data = True

        else:
            valid_data = False


name_function()






