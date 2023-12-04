str_first="1"
str_second=" "
str_third="2"
str_fourth=" "
str_fifth="3"
print("{}{}{}{}{}".format(str_first, str_second, str_third, str_fourth, str_fifth))
print("first_try")
str_second = str_first
str_first = " "
print("{}{}{}{}{}".format(str_first, str_second , str_third, str_fourth, str_fifth))
print("Second_try")
str_first = str_third
str_third = " "
print("{}{}{}{}{}".format(str_first, str_second, str_third, str_fourth, str_fifth))
print("third_try")
str_fourth = str_fifth
str_fifth = " "
print("{}{}{}{}{}".format(str_first, str_second, str_third, str_fourth, str_fifth))
print("fourth_try")
str_third = str_second
str_second = " "
print("{}{}{}{}{}".format(str_first, str_second, str_third, str_fourth, str_fifth))
print("fifth_try")
str_third = str_fourth
str_fourth = "1"
print("{}{}{}{}{}".format(str_first, str_second, str_third, str_fourth, str_fifth))
print("sixth_try")
str_second = str_third
str_third = " "
print("{}{}{}{}{}".format(str_first, str_second, str_third, str_fourth, str_fifth))
print("seventh_try")
str_first = str_second
str_second = "2"
print("{}{}{}{}{}".format(str_first, str_second, str_third, str_fourth, str_fifth))
print("eighth_try")
str_fifth = str_fourth
str_fourth = " "
print("{}{}{}{}{}".format(str_first, str_second, str_third, str_fourth, str_fifth))
print("nineth_try")
str_third = str_second
str_second = " "
print("{}{}{}{}{}".format(str_first, str_second, str_third, str_fourth, str_fifth))
