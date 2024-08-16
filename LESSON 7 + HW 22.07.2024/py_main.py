# LESSON 7 EX 3 HW

# START

# py_main.py

# i. Regular import of the whole file by its normal name
import py_func_my

# ii. Import the whole file with a shortened name (alias) mf
import py_func_my as mf

# iii. Import just the `print_stars` function from the file
from py_func_my import print_stars

# Using the imported functions
py_func_my.print_stars()  # Using the full module name
mf.print_stars()          # Using the alias name
print_stars()             # Using the directly imported function

# END

# *************
# *************
# *************


# START

# py_main.py

# Import the whole file by its normal name
import py_func_my

# Import the whole file with a shortened name (alias) mf
import py_func_my as mf

# Import just the `print_stars` function from the file
from py_func_my import print_stars

# Using the help function to see the documentation of `print_stars`
help(py_func_my.print_stars)
# Or using the alias
help(mf.print_stars)
# Or directly if the function was imported
help(print_stars)

# Using the imported functions
py_func_my.print_stars()  # Using the full module name
mf.print_stars()          # Using the alias name
print_stars()             # Using the directly imported function

# END

# Help on function print_stars in module py_func_my:
#
# print_stars()
#     Prints a line of asterisks (*************).
#
#     This function simply prints a line of 13 asterisks to the console.
#     It can be used to visually separate sections of output or for decorative purposes.
#
# Help on function print_stars in module py_func_my:
#
# print_stars()
#     Prints a line of asterisks (*************).
#
#     This function simply prints a line of 13 asterisks to the console.
#     It can be used to visually separate sections of output or for decorative purposes.
#
# Help on function print_stars in module py_func_my:
#
# print_stars()
#     Prints a line of asterisks (*************).
#
#     This function simply prints a line of 13 asterisks to the console.
#     It can be used to visually separate sections of output or for decorative purposes.
#
# *************
# *************
# *************