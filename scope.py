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