# ----------------------------------------------------------------------------------------
# What is a class?
# -----------------
#
# As a program gets larger and more complicated it is usually necessary to
# organise the code in some way to make it easier to manage. Classes are one
# of the tools available to programmers to do that.
#
# A class groups together some functions and some data variables under a
# common name, usually something that represents an important thing in your program.
#
# For example, if you had a program that was a video game you might choose to make classes
# for things like a level, a power up, a player or computer controlled enemies. Then each
# of those classes might have variables that store information like their speed, the images
# that show what it looks like or whether it is alive or dead.
# -----------------------------------------------------------------------------------------

# defining a really simple class


class MyClass:

    def __init__(self):
        self.my_variable = True

# the class above, called MyClass has one function, __init__ , and one variable, my_variable.
# You may have noticed the keyword 'self' in the function parameters and again before the variable name
# this keyword is used when defining classes in python and is what allows us to share the same variables
# between all the functions of the class. A variable like this is known as a member variable.
# try uncommenting the commented out line in the code below and running the code to see the difference
# between a member variable and a regular variable used in a class definition.


class TwoFunctions:
    
    def __init__(self, my_parameter):
        self.my_member_variable = my_parameter
        self.another_member_variable = 10
        
        a_non_member_variable = 5
        
    def a_second_function(self):
        print("Another member variable value: " + str(self.another_member_variable))
        # print("a_non_member_variable: " + str(a_non_member_variable))


# Creating an instance, or an object, from a class definition.
# -------------------------------------------------------------
#
# Often you will want to have multiple copies of a class in your
# code with only minimal differences. For example, having multiple enemies
# in a video game that behave identically apart from having different initial positions
# in the level. Because of this classes are designed like templates or moulds from which
# we can press out many instances.
#
# To create an instance you just write the class name, open some brackets and pass in any
# important startup data variables. Then you assign your newly created class to it's own variable
# which we can then use to access the classes member functions and data with the . operator.
#
# See below for an example of creating two different instances of the same class and of how to
# run (the commonly used term is 'call') a member function on an instance.

my_object = TwoFunctions(True)
my_second_object = TwoFunctions(False)
my_object.a_second_function()


# -----------------------------------------------------------------------
# CHALLENGE 1
# ------------
#
#  A) Create your own class called 'YourNameClass'.
#  B) Add an __init__ member function to it that takes two parameters called
#    'parameter_a' and 'parameter_b'
#  C) Store those parameters as member variables with the same names.
# -------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# CHALLENGE 2
# ------------
#
# Create a member function for your class called 'add' that adds together your
# two member variables and returns the result.
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# CHALLENGE 3
# ------------
#
# Create two instances of your class with different input arguments and then call
# the 'add' member function (also called method) on each of them.
#
# store the result in a variable and print that variable to the console
# ------------------------------------------------------------------------------
