#Local Scope
# A variable is only available from inside ther egion it is created.  This is called scope

# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function

def myfunc():
    x = 300
    print(x)

myfunc()

def myfunc2():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc2()


# Global Scope
# a variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from withhin any scope, global and local

# a variable created outside of a function is global and can be used by anyone:

y = 300

def myfunc3():
    print(y)

myfunc3()

print(y)